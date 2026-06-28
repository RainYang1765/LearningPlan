import networkx


def GraphFloyd(G: networkx.Graph):
    if not (G or networkx.is_weighted(G)):
        return None
    #
    dist = {}
    for node in G.nodes:
        dist[node] = {}
        for dst in G.nodes:
            dist[node][dst] = float("inf")
        dist[node][node] = 0
    for src, dst in G.edges:
        dist[src][dst] = G.edges[src, dst]["weight"]
        dist[dst][src] = G.edges[src, dst]["weight"]
    #
    for k in G.nodes:
        for i in G.nodes:
            for j in G.nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def DiGraphFloyd(DG: networkx.DiGraph):
    if not (DG or networkx.is_weighted(DG)):
        return None
    #
    dist = {}
    for node in DG.nodes:
        dist[node] = {}
        for dst in DG.nodes:
            dist[node][dst] = float("inf")
        dist[node][node] = 0
    for src, dst in DG.edges:
        dist[src][dst] = DG.edges[src, dst]["weight"]
    #
    for k in DG.nodes:
        for i in DG.nodes:
            for j in DG.nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
