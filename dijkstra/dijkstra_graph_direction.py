#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math, heapq
import numpy as np
import matplotlib.pyplot as plt

INF = math.inf

# ---- あなたの OHD（非対称＝有向）を貼る ----
OHD = np.array(
    [
        #  0    1    2    3    4    5
        [  0, 40,  15, INF, INF, INF],  # 0
        [ 40,  0,  20,  10,  12,   8],  # 1
        [ 15, 20,   0, 100, INF, INF],  # 2
        [INF, 10, 100,   0, INF, INF],  # 3
        [INF, 25, INF, INF,   0,   8],  # 4  ← 1↔4 が非対称（1→4=25, 4→1=12）
        [INF,  6, INF, INF,   8,   0],  # 5
    ],
    dtype=float,
)
SOURCE = 0


# ---- Dijkstra（有向） ----
def dijkstra_parent(dist_mat: np.ndarray, src: int):
    n = dist_mat.shape[0]
    dist = [INF] * n
    parent = [-1] * n
    dist[src] = 0.0
    pq = [(0.0, src)]
    seen = [False] * n
    while pq:
        d, u = heapq.heappop(pq)
        if seen[u]:
            continue
        seen[u] = True
        for v in range(n):
            w = dist_mat[u, v]
            if w == INF or w == 0:  # 自己ループ w=0 は無視
                continue
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, parent


dist, parent = dijkstra_parent(OHD, SOURCE)

# ---- 有向グラフを matplotlib だけで描画（簡易） ----
if __name__ == "__main__":
    import networkx as nx

    G = nx.DiGraph()
    n = OHD.shape[0]
    for i in range(n):
        for j in range(n):
            if i != j and OHD[i, j] != INF:
                G.add_edge(i, j, weight=OHD[i, j])

    pos = nx.spring_layout(G, seed=7)

    plt.figure(figsize=(8.5, 6.2))
    nx.draw_networkx_nodes(G, pos, node_color="#1f78b4", node_size=650)
    nx.draw_networkx_labels(G, pos, font_color="white", font_size=11)

    # 最短経路木の有向辺集合（parent[v] -> v）
    tree_edges = set()
    for v in range(n):
        if v != SOURCE and parent[v] != -1:
            tree_edges.add((parent[v], v))

    # 通常の矢印（グレー）
    other_edges = [e for e in G.edges() if e not in tree_edges]
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=other_edges,
        edge_color="#9aa0a6",
        width=1.8,
        arrows=True,
        arrowsize=18,
        connectionstyle="arc3,rad=0.07",
    )

    # 最短経路木の矢印（赤太線）
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=list(tree_edges),
        edge_color="#d62728",
        width=3.2,
        arrows=True,
        arrowsize=22,
        connectionstyle="arc3,rad=0.07",
    )

    # 重みラベル（方向別に表示）
    edge_labels = {(u, v): f"{int(G[u][v]['weight'])}" for (u, v) in G.edges()}
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, font_color="#333", font_size=10, label_pos=0.55
    )

    dist_str = "  ".join(
        f"{i}:{'Inf' if math.isinf(d) else int(d)}" for i, d in enumerate(dist)
    )
    plt.title(
        f"Dijkstra (directed) shortest-path tree from {SOURCE}\nDistances -> {dist_str}"
    )
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("dijkstra_directed_graph.png", dpi=300)
    plt.show()
