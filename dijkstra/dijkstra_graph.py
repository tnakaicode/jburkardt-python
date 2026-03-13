#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot the example graph from Burkardt's DIJKSTRA (Python) page and overlay the shortest-path tree.
Data source: people.sc.fsu.edu dijkstra (6 nodes, 8 links, nonnegative weights)
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# --- Example adjacency matrix (Inf means no edge), from Burkardt's page ---
# Nodes: 0..5
INF = math.inf
OHD = np.array(
    [
        [0, 40, 15, INF, INF, INF],
        [40, 0, 20, 10, 25, 6],
        [15, 20, 0, 100, INF, INF],
        [INF, 10, 100, 0, INF, INF],
        [INF, 25, INF, INF, 0, 8],
        [INF, 6, INF, INF, 8, 0],
    ],
    dtype=float,
)

SOURCE = 0  # start node

# --- Dijkstra (heap-based) to compute parent tree for plotting ---
import heapq


def dijkstra_parent_tree(dist_mat: np.ndarray, src: int):
    n = dist_mat.shape[0]
    dist = [math.inf] * n
    parent = [-1] * n
    dist[src] = 0.0
    pq = [(0.0, src)]
    visited = [False] * n

    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v in range(n):
            w = dist_mat[u, v]
            if w == math.inf or w == 0:
                continue
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, parent


dist, parent = dijkstra_parent_tree(OHD, SOURCE)

# --- Build edge list ---
edges = []
weights = {}
n = OHD.shape[0]
for i in range(n):
    for j in range(i + 1, n):
        if OHD[i, j] != math.inf:
            edges.append((i, j))
            weights[(i, j)] = OHD[i, j]


# --- Plot with networkx if available; otherwise fallback ---
def draw_with_networkx():
    import networkx as nx

    G = nx.Graph()
    G.add_nodes_from(range(n))
    for u, v in edges:
        G.add_edge(u, v, weight=weights[(u, v)])

    # layout: spring; you can seed for reproducibility
    pos = nx.spring_layout(G, seed=7)

    # draw base graph
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, node_color="#1f78b4", node_size=600)
    nx.draw_networkx_labels(G, pos, font_color="white", font_size=11)

    # edge colors/thickness
    edge_colors = []
    edge_widths = []
    tree_edges = set()
    for v in range(n):
        if v != SOURCE and parent[v] != -1:
            a, b = sorted((v, parent[v]))
            tree_edges.add((a, b))
    for u, v in G.edges():
        if (min(u, v), max(u, v)) in tree_edges:
            edge_colors.append("#d62728")  # red for tree
            edge_widths.append(3.2)
        else:
            edge_colors.append("#999999")
            edge_widths.append(1.5)

    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=edge_widths)

    # edge labels (weights)
    wl = {(u, v): f"{G[u][v]['weight']:.0f}" for (u, v) in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=wl, font_color="#333333")

    # title with distances
    dist_str = "  ".join(
        f"{i}:{(0 if math.isclose(d,0) else int(d))}" for i, d in enumerate(dist)
    )
    plt.title(f"Dijkstra shortest-path tree from {SOURCE}\nDistances -> {dist_str}")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("dijkstra_graph.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    import networkx as _nx  # noqa
    draw_with_networkx()
