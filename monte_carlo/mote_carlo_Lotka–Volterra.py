#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monte Carlo ensemble of ODE trajectories with variability in initial conditions
and parameters. 既定は Lotka–Volterra（軌道が分かりやすい相平面）でデモ。

依存: numpy, matplotlib（SciPy不要：自前RK4）
"""

from __future__ import annotations
from pdb import main
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Callable, Dict, Tuple, List, Any, Optional


# ------------------------------------------------------------
# 数値積分（自前 RK4）
# ------------------------------------------------------------
def rk4(
    rhs: Callable[[float, np.ndarray, Dict[str, float]], np.ndarray],
    t0: float,
    y0: np.ndarray,
    t1: float,
    dt: float,
    params: Dict[str, float],
) -> Tuple[np.ndarray, np.ndarray]:
    """
    右辺 rhs(t, y, params) の ODE を [t0, t1] 区間で刻み dt で RK4 積分
    戻り: t (nt,), Y (nt, ny)
    """
    nstep = int(np.ceil((t1 - t0) / dt))
    t = np.linspace(t0, t1, nstep + 1)
    y = np.zeros((nstep + 1, len(y0)), dtype=float)
    y[0] = y0

    for k in range(nstep):
        h = t[k + 1] - t[k]  # 最後だけ dt が微調整されることがある
        tk = t[k]
        yk = y[k]
        k1 = rhs(tk, yk, params)
        k2 = rhs(tk + 0.5 * h, yk + 0.5 * h * k1, params)
        k3 = rhs(tk + 0.5 * h, yk + 0.5 * h * k2, params)
        k4 = rhs(tk + h, yk + h * k3, params)
        y[k + 1] = yk + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

        # 物理量の負値を避けたい（例：個体数）場合の簡易クリップ
        # y[k+1] = np.maximum(y[k+1], 0.0)

    return t, y


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


# 既定モデル（差し替え可）
LV_MODEL = ModelSpec(
    rhs=lotka_volterra_rhs,
    state_names=("Prey x", "Predator y"),
    default_params={"alpha": 1.0, "beta": 0.5, "gamma": 1.5, "delta": 0.75},
    default_y0=np.array([2.0, 1.0], dtype=float),
)


# ------------------------------------------------------------
# サンプリング（初期値・パラメータ）
#   - uniform(low, high)
#   - normal(mu, sigma, clip_low=None, clip_high=None)
# ------------------------------------------------------------
def sample_value(spec: Tuple, rng: np.random.Generator) -> float:
    kind = spec[0]
    if kind == "uniform":
        _, low, high = spec
        return float(rng.uniform(low, high))
    elif kind == "normal":
        # ( "normal", mu, sigma, clip_low, clip_high )
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
# Monte Carlo 本体
# ------------------------------------------------------------
def run_monte_carlo(
    model: ModelSpec,
    t_span: Tuple[float, float],
    dt: float,
    N: int,
    param_samplers: Dict[str, Tuple],
    y0_samplers: Dict[str, Tuple],
    seed: Optional[int] = 20260311,
) -> Dict[str, Any]:
    """
    N 本の軌道を Monte Carlo で生成
    戻り: dict  { "t": (nt,), "traj": (N, nt, ny), "params": [...], "y0s": (N, ny) }
    """
    rng = np.random.default_rng(seed)
    ny = len(model.state_names)

    # 時間軸を先に決めておく（全サンプル共通）
    t0, t1 = t_span
    nt = int(np.ceil((t1 - t0) / dt)) + 1
    t = np.linspace(t0, t1, nt)

    traj = np.zeros((N, nt, ny), dtype=float)
    plist: List[Dict[str, float]] = []
    y0s = np.zeros((N, ny), dtype=float)

    # y0_samplers のキー順を state_names に合わせる
    y0_keys = list(y0_samplers.keys()) if y0_samplers else list(model.state_names)

    for n in range(N):
        # パラメータと初期値をサンプル
        p = model.default_params.copy()
        if param_samplers:
            p.update(sample_dict(param_samplers, rng))
        plist.append(p)

        y0 = model.default_y0.copy()
        if y0_samplers:
            y0 = np.array(
                [sample_value(y0_samplers[k], rng) for k in y0_keys], dtype=float
            )
        y0s[n] = y0

        # 積分（RK4）
        t_, y = rk4(model.rhs, t0, y0, t1, dt, p)

        # 念のため、時間ベクトル整合をチェック（最後だけ dt が合わない可能性に対応）
        if len(t_) != nt:
            # 長さが違う場合は再サンプリング兼ねて最終的に補間（ほぼ起きない）
            y_interp = np.vstack([np.interp(t, t_, y[:, i]) for i in range(ny)]).T
            traj[n] = y_interp
        else:
            traj[n] = y

    return {
        "t": t,
        "traj": traj,
        "params": plist,
        "y0s": y0s,
        "state_names": model.state_names,
    }


# ------------------------------------------------------------
# 可視化
# ------------------------------------------------------------
def plot_phase_spaghetti(ax, t, traj, idx_xy=(0, 1), color="#1f77b4", alpha=0.35):
    """
    相平面（x-y）に N 本の軌道を重ね描き
    traj: (N, nt, ny)
    """
    ix, iy = idx_xy
    for y in traj:
        ax.plot(y[:, ix], y[:, iy], color=color, alpha=alpha, lw=1.2)
    ax.set_xlabel(f"{idx_xy[0]}: ")
    ax.set_xlabel(f"{idx_xy[0]}")
    ax.set_ylabel(f"{idx_xy[1]}")
    ax.grid(True, alpha=0.25)


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
    """
    時系列 x_i(t) のスパゲティ＋信頼帯（分位）＋平均
    """
    X = traj[:, :, var_index]  # (N, nt)
    # スパゲティ
    for x in X:
        ax.plot(t, x, color=color, alpha=0.15, lw=1.0)
    # 信頼帯
    lo = np.percentile(X, band[0], axis=0)
    hi = np.percentile(X, band[1], axis=0)
    ax.fill_between(
        t, lo, hi, color=color, alpha=0.25, label=f"{band[0]}–{band[1]}% band"
    )
    # 平均
    mu = X.mean(axis=0)
    ax.plot(t, mu, color=mean_color, lw=2.0, label="mean")
    ax.set_xlabel("t")
    ax.set_ylabel(f"state[{var_index}]")
    if label:
        ax.set_title(label)
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best", framealpha=0.8)


def plot_final_scatter(ax, traj, idx_xy=(0, 1), color="#1f77b4"):
    """
    終点 (x(T), y(T)) の散布図
    """
    ix, iy = idx_xy
    XY = traj[:, -1, [ix, iy]]
    ax.scatter(XY[:, 0], XY[:, 1], s=18, c=color, alpha=0.7, edgecolor="none")
    ax.set_xlabel(f"{idx_xy[0]}_final")
    ax.set_ylabel(f"{idx_xy[1]}_final")
    ax.grid(True, alpha=0.25)


# ------------------------------------------------------------
# メイン：デモ実行
# ------------------------------------------------------------
if __name__ == "__main__":
    # --------- 設定 ---------
    model = LV_MODEL  # ここを自作モデルに差し替え可
    t_span = (0.0, 15.0)
    dt = 0.01
    N = 300  # サンプル数（重い場合は 100 前後に）
    seed = 20260311

    # パラメータのばらつき（例：一様分布）
    #  例）alpha ~ U[0.9, 1.1], beta ~ U[0.45, 0.55], ...
    param_samplers = {
        "alpha": ("uniform", 0.9, 1.1),
        "beta": ("uniform", 0.45, 0.55),
        "gamma": ("uniform", 1.3, 1.7),
        "delta": ("uniform", 0.65, 0.85),
    }

    # 初期値のばらつき（例：正規分布 + クリップ）
    y0_samplers = {
        "Prey x": ("normal", 2.0, 0.25, 0.05, None),  # μ=2, σ=0.25, 最低0.05
        "Predator y": ("normal", 1.0, 0.20, 0.05, None),
    }

    # --------- Monte Carlo 実行 ---------
    out = run_monte_carlo(model, t_span, dt, N, param_samplers, y0_samplers, seed=seed)
    t = out["t"]
    traj = out["traj"]  # (N, nt, ny)

    # --------- 可視化 ---------
    fig = plt.figure(figsize=(12, 8))

    # (1) 相平面のスパゲティ（x vs y）
    ax1 = fig.add_subplot(2, 2, 1)
    for y in traj:
        ax1.plot(y[:, 0], y[:, 1], color="#1f77b4", alpha=0.25, lw=1.0)
    ax1.set_xlabel("x (Prey)")
    ax1.set_ylabel("y (Predator)")
    ax1.set_title("Phase plane: trajectory ensemble")
    ax1.grid(True, alpha=0.25)

    # (2) x(t) の信頼帯 + 平均
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

    # (3) y(t) の信頼帯 + 平均
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

    # (4) 最終点の散布図
    ax4 = fig.add_subplot(2, 2, 4)
    plot_final_scatter(ax4, traj, idx_xy=(0, 1), color="#ff7f0e")
    ax4.set_title("Scatter of endpoints (x(T), y(T))")

    fig.suptitle(
        "Monte Carlo trajectories with parameter/initial-condition variability (Lotka–Volterra)"
    )
    plt.tight_layout()
    plt.show()
