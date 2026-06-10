import networkx


def GraphBFS(G: networkx.Graph):
    if not G:
        return None
    #
    from collections import deque

    #
    visit = {}
    for node in G.nodes:
        visit[node] = False
    for node in G.nodes:
        if not visit[node]:
            L = deque([node])
            while L:
                node = L.popleft()
                if not visit[node]:
                    visit[node] = True
                    print(f"Visiting node {node}")
                    for _, dst in G.edges(node):
                        if not visit[dst]:
                            L.append(dst)


def DiGraphBFS(DG: networkx.DiGraph):
    if not DG:
        return None
    #
    from collections import deque

    #
    visit = {}
    for node in DG.nodes:
        visit[node] = False
    for node in DG.nodes:
        if not visit[node]:
            L = deque([node])
            while L:
                node = L.popleft()
                if not visit[node]:
                    visit[node] = True
                    print(f"Visiting node {node}")
                    for _, dst in DG.out_edges(node):
                        if not visit[dst]:
                            L.append(dst)


def GraphDFS(G: networkx.Graph):
    """
    depth first search in G
    """
    if not G:
        return None

    def _GDFS(G: networkx.Graph, start_node, visit: dict):
        visit[start_node] = True
        print(f"Visiting node {start_node}")
        for _, dst in G.edges(start_node):
            if not visit[dst]:
                _GDFS(G, dst, visit)

    visit_flag = {}
    for node in G.nodes:
        visit_flag[node] = False
    for node in G.nodes:
        if not visit_flag[node]:
            _GDFS(G, node, visit_flag)


def DiGraphDFS(DG: networkx.DiGraph):
    """
    depth first search in DG
    """
    if not DG:
        return None

    def _DGDFS(DG: networkx.DiGraph, start_node, visit: dict):
        visit[start_node] = True
        print(f"Visiting node {start_node}")
        for _, dst in DG.out_edges(start_node):
            if not visit[dst]:
                _DGDFS(DG, dst, visit)

    visit_flag = {}
    for node in DG.nodes:
        visit_flag[node] = False
    for node in DG.nodes:
        if not visit_flag[node]:
            _DGDFS(DG, node, visit_flag)
