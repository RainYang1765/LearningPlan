# REAL825 魔法路径
# https://www.nowcoder.com/share/jump/8045440981781593814300

import heapq

inf = float("inf")


# def Dijkstra(n, k_level, dist, a, adj):
#     pq = []
#     for i in range(1, n + 1):
#         if dist[i][k_level] != inf:
#             heapq.heappush(pq, (dist[i][k_level], i))
#     while pq:
#         d, u = heapq.heappop(pq)
#         if d > dist[u][k_level]:
#             continue
#         for v, w in adj[u]:
#             cost = w + (a[v] if a[v] >= 0 else 0)
#             if (
#                 dist[u][k_level] != inf
#                 and dist[u][k_level] + cost < dist[v][k_level]
#             ):
#                 dist[v][k_level] = dist[u][k_level] + cost
#                 heapq.heappush(pq, (dist[v][k_level], v))


def Dijkstra(n, k_level, dist, adj):
    L = []
    for i in range(1, n + 1):
        if dist[i][k_level] != inf:
            heapq.heappush(L, (dist[i][k_level], i))
    while L:
        node_weight, node = heapq.heappop(L)
        if node_weight > dist[node][k_level]:
            continue
        for neighbor, weight in adj[node]:
            if (
                dist[node][k_level] != inf
                and dist[node][k_level] + weight < dist[neighbor][k_level]
            ):
                dist[neighbor][k_level] = dist[node][k_level] + weight
                heapq.heappush(L, (dist[neighbor][k_level], neighbor))


def solve():
    n, m, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    G: list[set[tuple[int, int]]] = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        G[u].add((v, w + (a[v] if a[v] > 0 else 0)))
        G[v].add((u, w + (a[u] if a[u] > 0 else 0)))
    dist = [[inf for _ in range(k + 1)] for _ in range(n + 1)]
    dist[1][0] = 0
    Dijkstra(n, 0, dist, G)
    for k_used in range(k):
        # 继承
        for i in range(1, n + 1):
            dist[i][k_used + 1] = dist[i][k_used]
        # 转移
        for u in range(1, n + 1):
            if dist[u][k_used] != inf:
                for v, w in G[u]:
                    if a[v] < 0:
                        new_weight = dist[u][k_used] + w + a[v]
                        if dist[v][k_used + 1] > new_weight:
                            dist[v][k_used + 1] = new_weight
        Dijkstra(n, k_used + 1, dist, G)
    min_dist = dist[n][k]
    if min_dist == inf:
        print("NO")
    else:
        print(min_dist)


if __name__ == "__main__":
    solve()
    exit()
