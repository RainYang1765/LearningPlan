from collections import deque

import networkx, copy
from matplotlib import pyplot as plt


def PrintGraph(DWG: networkx.DiGraph | networkx.Graph, weight: bool = False):
    pos = networkx.circular_layout(DWG)
    networkx.draw_networkx_nodes(DWG, pos=pos)
    networkx.draw_networkx_edges(DWG, pos=pos)
    networkx.draw_networkx_labels(DWG, pos=pos)
    if weight:
        weight_labels = networkx.get_edge_attributes(DWG, "weight")
        networkx.draw_networkx_edge_labels(DWG, pos=pos, edge_labels=weight_labels)
    plt.show()
    return

def GBFS(G:networkx.Graph):
    if not G:
        return None
    #
    from collections import deque
    #
    visit={}
    for node in G.nodes:
        visit[node] = False
    for node in G.nodes:
        if not visit[node]:
            L=deque([node])
            while L:
                node=L.popleft()
                if not visit[node]:
                    visit[node] = True
                    print(f"Visiting node {node}")
                    for _,dst in G.edges(node):
                        if not visit[dst]:
                            L.append(dst)


def GShortestPath(G: networkx.Graph, src_node: str, dst_node: str):
    """
    find the shortest path from src to dst in G, ignoring weights
    """
    if not (G or src_node or dst_node):
        return None
    if not G.has_node(src_node) or not G.has_node(dst_node):
        return None
    #
    dist = {}
    for node in G.nodes:
        dist[node] = float("inf")
    dist[src_node] = 0
    # deque has higher performance than list when poping from the left
    from collections import deque

    visit = deque([src_node])
    #
    while visit:
        node = visit.popleft()
        for _, dst in G.edges(node):
            if dist[dst] > dist[node] + 1:
                dist[dst] = dist[node] + 1
                visit.append(dst)
    return dist[dst_node] if dist[dst_node] != float("inf") else None


def DGShortestPath(DG: networkx.DiGraph, src_node: str, dst_node: str):
    """
    find the shortest path from src to dst in DG, ignoring weights
    """
    if not (DG or src_node or dst_node):
        return None
    if not DG.has_node(src_node) or not DG.has_node(dst_node):
        return None
    #
    dist = {}
    for node in DG.nodes:
        dist[node] = float("inf")
    dist[src_node] = 0
    # deque has higher performance than list when poping from the left
    from collections import deque

    visit = deque([src_node])
    #
    while visit:
        node = visit.popleft()
        for _, dst in DG.out_edges(node):
            if dist[dst] > dist[node] + 1:
                dist[dst] = dist[node] + 1
                visit.append(dst)
    return dist[dst_node] if dist[dst_node] != float("inf") else None


def WGDijkstraShortestPath(G: networkx.Graph, src_node: str, dst_node: str):
    """
    find the shortest path from src to dst in WG, considering weights
    """
    if not (G or src_node or dst_node):
        return None
    if not G.has_node(src_node) or not G.has_node(dst_node):
        return None
    #
    dist = {}
    for node in G.nodes:
        dist[node] = float("inf")
    dist[src_node] = 0
    # deque has higher performance than list when poping from the left
    from collections import deque

    visit = deque([src_node])
    #
    while visit:
        node = visit.popleft()
        for _, dst in G.edges(node):
            weight = G[node][dst].get("weight")
            if dist[dst] > dist[node] + weight:
                dist[dst] = dist[node] + weight
                visit.append(dst)
    return dist[dst_node] if dist[dst_node] != float("inf") else None


def DWGDijkstraShortestPath(DWG: networkx.DiGraph, src_node: str, dst_node: str):
    """
    find the shortest path from src to dst in DWG, considering weights
    """
    if not (DWG or src_node or dst_node):
        return None
    if not DWG.has_node(src_node) or not DWG.has_node(dst_node):
        return None
    #
    dist = {}
    detect = {}
    path={}
    for node in DWG.nodes:
        dist[node] = float("inf")
        detect[node] = False
        path[node]=[]
    dist[src_node] = 0
    detect[src_node] = True
    # deque has higher performance than list when poping from the left
    from collections import deque

    visit = deque([src_node])
    #
    while visit:
        node = visit.popleft()
        for _, dst in DWG.out_edges(node):
            weight = DWG[node][dst].get("weight")
            if dist[dst] > dist[node] + weight and not detect[dst]:
                dist[dst] = dist[node] + weight
                detect[dst] = True
                visit.append(dst)
                path[node].append(dst)
    return dist[dst_node] if dist[dst_node] != float("inf") else None


def DWGFloydShortestPath(DWG: networkx.DiGraph):
    """
    find the shortest path from src to dst in DWG, considering weights
    """
    if not DWG:
        return None 
    #
    dist = {}
    for node in DWG.nodes:
        dist[node] = {}
        for dst in DWG.nodes:
            if node == dst:
                dist[node][dst] = 0
            elif DWG.has_edge(node, dst):
                dist[node][dst] = DWG[node][dst].get("weight")
            else:
                dist[node][dst] = float("inf")
    #
    for k in DWG.nodes:
        for i in DWG.nodes:
            for j in DWG.nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def GDFS(G:networkx.Graph):
    """
    depth first search in G
    """
    if not G:
        return None
    def _GDFS(G:networkx.Graph,start_node,visit:dict):
        visit[start_node] = True
        print(f"Visiting node {start_node}")
        for _,dst in G.edges(start_node):
            if not visit[dst]:
                _GDFS(G,dst,visit)
    visit_flag={}
    for node in G.nodes:
        visit_flag[node] = False
    for node in G.nodes:
        if not visit_flag[node]:
            _GDFS(G,node,visit_flag)


if __name__ == "__main__":
    DWG_maxflow=networkx.DiGraph()
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
    PrintGraph(DWG_maxflow, weight=True)
    DWGDijkstraShortestPath(DWG_maxflow, "s", "t")
    G=networkx.Graph()
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
    GBFS(G)
    DG = networkx.DiGraph()
    DG.add_edges_from(
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
    PrintGraph(DG)
    # result = DGShortestPath(DG,"C","D")
    # print(result)
    DWG = networkx.DiGraph()
    DWG.add_weighted_edges_from(
        [
            ("A", "B", 2),
            ("A", "C", 1),
            ("B", "D", 3),
            ("B", "E", 4),
            ("C", "F", 2),
            ("C", "G", 6),
            ("G", "A", 7),
            ("G", "F", 2),
            ("F", "E", 4),
            ("E", "C", 6),
        ]
    )
    # PrintGraph(DWG, weight=True)
    # result = DWGDijkstraShortestPath(DWG, "C", "D")
    # print(result)
