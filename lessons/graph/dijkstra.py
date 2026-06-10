import networkx


def GraphDijkstra(G: networkx.Graph, src, dst) -> tuple | None:
    if not (G or src or dst):
        return None
    #
    if not G.has_node(src) or not G.has_node(dst):
        return None
    #
    dist = {}
    prev = {}
    path = []
    for node in G.nodes:
        dist[node] = float("inf")
        prev[node] = None
    dist[src] = 0
    #
    from collections import deque

    visit = deque([src])
    #
    while visit:
        node = visit.popleft()
        for _, dst in G.edges(node):
            if dist[dst] > dist[node] + 1:
                dist[dst] = dist[node] + 1
                prev[dst] = node
                visit.append(dst)
    #
    node = dst
    while node:
        if prev[node]:
            path.append((prev[node], node))
        node = prev[node]
    return (dist[dst], path[::-1]) if dist[dst] != float("inf") else None


def DiGraphDijkstra(DG: networkx.DiGraph, src, dst) -> tuple | None:
    if not (DG or src or dst):
        return None
    #
    if not DG.has_node(src) or not DG.has_node(dst):
        return None
    #
    dist = {}
    prev = {}
    path = []
    for node in DG.nodes:
        dist[node] = float("inf")
        prev[node] = None
    dist[src] = 0
    #
    from collections import deque

    visit = deque([src])
    #
    while visit:
        node = visit.popleft()
        for _, neighbor in DG.out_edges(node):
            new_w = dist[node] + DG.edges[node, neighbor]["weight"]
            if dist[neighbor] > new_w:
                dist[neighbor] = new_w
                prev[neighbor] = node
                visit.append(neighbor)
    #
    node = dst
    while node:
        if prev[node]:
            path.append((prev[node], node))
        node = prev[node]
    return (dist[dst], path[::-1]) if dist[dst] != float("inf") else None


if __name__ == "__main__":
    G = networkx.Graph()
    G.add_edges_from(
        [
            ("A", "B"),
            ("A", "C"),
            ("B", "D"),
            ("B", "E"),
            ("C", "F"),
            ("C", "G"),
            ("G", "A"),
            ("G", "F"),
            ("F", "E"),
            ("E", "C"),
        ]
    )
    #
    DWG_maxflow = networkx.DiGraph()
    DWG_maxflow.add_weighted_edges_from(
        [
            ("s", "b", 2),
            ("s", "a", 3),
            ("a", "b", 1),
            ("a", "c", 3),
            ("a", "d", 4),
            ("b", "d", 2),
            ("c", "t", 2),
            ("d", "t", 3),
        ]
    )
    dist_path = DiGraphDijkstra(DWG_maxflow, "s", "t")
    dist = path = None
    if dist_path:
        dist, path = dist_path
    print(f"Shortest path from s to t is {dist} with path {path}")
