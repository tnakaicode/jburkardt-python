#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monte Carlo ensemble of ODE trajectories with variability in initial conditions
and parameters, solved by SciPy's solve_ivp (Runge–Kutta: RK45).
"""

from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Callable, Dict, Tuple, List, Any, Optional
from scipy.integrate import solve_ivp


# ------------------------------------------------------------
# 例: Lotka–Volterra（捕食-被食）
#   x' = alpha*x - beta*x*y
#   y' = delta*x*y - gamma*y
# ------------------------------------------------------------
def lotka_volterra_rhs(t: float, y: np.ndarray, p: Dict[str, float]) -> np.ndarray:
    x, z = y  # x=prey, z=predator
    alpha = p["alpha"]
    beta = p["beta"]
    gamma = p["gamma"]
    delta = p["delta"]
    dx = alpha * x - beta * x * z
    dz = delta * x * z - gamma * z
    return np.array([dx, dz], dtype=float)


@dataclass
class ModelSpec:
    rhs: Callable[[float, np.ndarray, Dict[str, float]], np.ndarray]
    state_names: Tuple[str, ...]
    default_params: Dict[str, float]
    default_y0: np.ndarray


# ------------------------------------------------------------
# サンプリングユーティリティ
#   - uniform(low, high)
#   - normal(mu, sigma, clip_low=None, clip_high=None)
# ------------------------------------------------------------
def sample_value(spec: Tuple, rng: np.random.Generator) -> float:
    kind = spec[0]
    if kind == "uniform":
        _, low, high = spec
        return float(rng.uniform(low, high))
    elif kind == "normal":
        mu, sig = spec[1], spec[2]
        clip_low = spec[3] if len(spec) > 3 else None
        clip_high = spec[4] if len(spec) > 4 else None
        v = float(rng.normal(mu, sig))
        if clip_low is not None:
            v = max(v, clip_low)
        if clip_high is not None:
            v = min(v, clip_high)
        return v
    else:
        raise ValueError(f"unknown sampler: {kind}")


def sample_dict(
    template: Dict[str, Tuple], rng: np.random.Generator
) -> Dict[str, float]:
    return {k: sample_value(v, rng) for k, v in template.items()}


# ------------------------------------------------------------
# Monte Carlo 本体（SciPy solve_ivp, RK45）
# ------------------------------------------------------------
def run_monte_carlo_scipy(
    model: ModelSpec,
    t_span: Tuple[float, float],
    dt_out: float,
    N: int,
    param_samplers: Dict[str, Tuple],
    y0_samplers: Dict[str, Tuple],
    rtol: float = 1e-6,
    atol: float = 1e-9,
    max_step: Optional[float] = None,
    seed: Optional[int] = 20260311,
) -> Dict[str, Any]:
    """
    SciPy solve_ivp(RK45) で N 本の軌道を Monte Carlo 生成。
    出力は等間隔 t_eval（dt_out）でそろえる。
    """
    rng = np.random.default_rng(seed)
    ny = len(model.state_names)

    t0, t1 = t_span
    nt = int(np.ceil((t1 - t0) / dt_out)) + 1
    t_eval = np.linspace(t0, t1, nt)

    traj = np.zeros((N, nt, ny), dtype=float)
    plist: List[Dict[str, float]] = []
    y0s = np.zeros((N, ny), dtype=float)
    failures = 0

    for n in range(N):
        # パラメータ・初期値をサンプル
        p = model.default_params.copy()
        if param_samplers:
            p.update(sample_dict(param_samplers, rng))
        plist.append(p)

        y0 = model.default_y0.copy()
        if y0_samplers:
            # state_names に合わせて並べる
            y0 = np.array(
                [sample_value(y0_samplers[name], rng) for name in model.state_names],
                dtype=float,
            )
        y0s[n] = y0

        # SciPy solve_ivp（RK45）
        fun = lambda tt, yy: model.rhs(tt, yy, p)

        ms = np.inf if (max_step is None) else max_step
        sol = solve_ivp(
            fun,
            t_span=(t0, t1),
            y0=y0,
            method="RK45",
            t_eval=t_eval,
            rtol=rtol,
            atol=atol,
            max_step=ms,
        )

        if not sol.success or sol.y.shape[1] != nt:
            failures += 1
            # 失敗時は NaN で埋めるか、簡易再トライ等を行う
            traj[n] = np.nan
        else:
            traj[n] = sol.y.T

    if failures > 0:
        print(
            f"[warn] solver failed for {failures}/{N} samples (NaN filled). "
            f"Try relaxing tolerances or setting max_step."
        )

    return {
        "t": t_eval,
        "traj": traj,
        "params": plist,
        "y0s": y0s,
        "state_names": model.state_names,
    }


# ------------------------------------------------------------
# 可視化
# ------------------------------------------------------------
def plot_timeseries_with_band(
    ax,
    t,
    traj,
    var_index=0,
    color="#1f77b4",
    band=(5, 95),
    mean_color="#d62728",
    label=None,
):
    """時系列のスパゲティ＋信頼帯（分位）＋平均"""
    X = traj[:, :, var_index]  # (N, nt)
    # NaN を除去
    X = X[~np.isnan(X).any(axis=1)]
    for x in X:
        ax.plot(t, x, color=color, alpha=0.15, lw=1.0)
    if X.size:
        lo = np.percentile(X, band[0], axis=0)
        hi = np.percentile(X, band[1], axis=0)
        mu = X.mean(axis=0)
        ax.fill_between(
            t, lo, hi, color=color, alpha=0.25, label=f"{band[0]}–{band[1]}% band"
        )
        ax.plot(t, mu, color=mean_color, lw=2.0, label="mean")
    ax.set_xlabel("t")
    ax.set_ylabel(f"state[{var_index}]")
    if label:
        ax.set_title(label)
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best", framealpha=0.8)


def plot_final_scatter(ax, traj, idx_xy=(0, 1), color="#1f77b4"):
    """最終点 (x(T), y(T)) の散布図"""
    ix, iy = idx_xy
    XY = traj[:, -1, [ix, iy]]
    XY = XY[~np.isnan(XY).any(axis=1)]
    ax.scatter(XY[:, 0], XY[:, 1], s=18, c=color, alpha=0.7, edgecolor="none")
    ax.set_xlabel(f"{idx_xy[0]}_final")
    ax.set_ylabel(f"{idx_xy[1]}_final")
    ax.grid(True, alpha=0.25)


# ------------------------------------------------------------
# デモ実行
# ------------------------------------------------------------
if __name__ == "__main__":
    # 既定モデル（差し替え可）
    LV_MODEL = ModelSpec(
        rhs=lotka_volterra_rhs,
        state_names=("Prey x", "Predator y"),
        default_params={"alpha": 1.0, "beta": 0.5, "gamma": 1.5, "delta": 0.75},
        default_y0=np.array([2.0, 1.0], dtype=float),
    )

    # --------- 設定（必要に応じて変更） ---------
    model = LV_MODEL
    t_span = (0.0, 15.0)
    dt_out = 0.02  # 出力間隔（プロット解像度）
    N = 300  # サンプル本数（重いときは 100 前後に）
    seed = 20260311

    # パラメータばらつき（例：一様分布）
    param_samplers = {
        "alpha": ("uniform", 0.9, 1.1),
        "beta": ("uniform", 0.45, 0.55),
        "gamma": ("uniform", 1.3, 1.7),
        "delta": ("uniform", 0.65, 0.85),
    }

    # 初期値ばらつき（例：正規分布＋下限クリップ）
    y0_samplers = {
        "Prey x": ("normal", 2.0, 0.25, 0.05, None),
        "Predator y": ("normal", 1.0, 0.20, 0.05, None),
    }

    # SciPy solver の精度パラメータ
    rtol = 1e-6
    atol = 1e-9
    max_step = None  # 硬い系でステップが暴れるときは 0.05 など上限を与える

    # --------- Monte Carlo ---------
    out = run_monte_carlo_scipy(
        model,
        t_span,
        dt_out,
        N,
        param_samplers,
        y0_samplers,
        rtol=rtol,
        atol=atol,
        max_step=max_step,
        seed=seed,
    )
    t = out["t"]
    traj = out["traj"]  # (N, nt, ny)

    # --------- 可視化 ---------
    fig = plt.figure(figsize=(12, 8))

    # (1) 相平面（x vs y）スパゲティ
    ax1 = fig.add_subplot(2, 2, 1)
    valid = traj[~np.isnan(traj).any(axis=(1, 2))]
    for y in valid:
        ax1.plot(y[:, 0], y[:, 1], color="#1f77b4", alpha=0.25, lw=1.0)
    ax1.set_xlabel("x (Prey)")
    ax1.set_ylabel("y (Predator)")
    ax1.set_title("Phase plane: trajectory ensemble")
    ax1.grid(True, alpha=0.25)

    # (2) x(t) の信頼帯＋平均
    ax2 = fig.add_subplot(2, 2, 2)
    plot_timeseries_with_band(
        ax2,
        t,
        traj,
        var_index=0,
        color="#1f77b4",
        band=(5, 95),
        mean_color="#d62728",
        label="x(t) with 5–95% band",
    )

    # (3) y(t) の信頼帯＋平均
    ax3 = fig.add_subplot(2, 2, 3)
    plot_timeseries_with_band(
        ax3,
        t,
        traj,
        var_index=1,
        color="#17becf",
        band=(5, 95),
        mean_color="#d62728",
        label="y(t) with 5–95% band",
    )

    # (4) 最終点散布図
    ax4 = fig.add_subplot(2, 2, 4)
    plot_final_scatter(ax4, traj, idx_xy=(0, 1), color="#ff7f0e")
    ax4.set_title("Scatter of endpoints (x(T), y(T))")

    fig.suptitle("Monte Carlo trajectories (Lotka–Volterra) (SciPy solve_ivp RK45)")
    plt.tight_layout()
    plt.savefig("monte_carlo_lotka_volterra.png", dpi=300)
    plt.show()
