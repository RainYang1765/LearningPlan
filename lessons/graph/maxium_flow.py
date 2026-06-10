import networkx
from dijkstra import DiGraphDijkstra
import matplotlib.pyplot as plt
from netgraph import Graph
import copy


def ShowGraph(G: networkx.DiGraph | networkx.Graph):
    edge_labels = {}
    for edge in G.edges:
        edge_labels[edge] = G.edges[*edge]["weight"]
    Graph(
        G,
        arrows=True,
        node_labels=True,
        edge_labels=edge_labels,
        edge_color="black",
        edge_width=1,
        edge_layout="curved",
        edge_layout_kwargs=dict(bundle_parallel_edges=False),
    )
    plt.show()
    return


def DiGraphMaxiumFlow(DG: networkx.DiGraph):
    if not (DG or networkx.is_weighted(DG)):
        return None
    #
    DGf = copy.deepcopy(DG)
    s = None
    t = None
    max_flow: float = 0
    for node in DGf.nodes:
        if DGf.in_degree(node) == 0:
            s = node
            continue
        elif DGf.out_degree(node) == 0:
            t = node
            continue
        elif s and t:
            break
    #
    if not (s and t):
        raise networkx.NetworkXError("Illegal Flow Network!")
    #
    weight_path = DiGraphDijkstra(DGf, s, t)
    while weight_path:
        _, path = weight_path
        minimal_flow: float = float("inf")
        for edge in path:
            w = DGf.edges[edge[0], edge[1]]["weight"]
            if minimal_flow > w:
                minimal_flow = w
        if minimal_flow == float("inf"):
            return minimal_flow
        #
        for edge in path:
            w = DGf.edges[edge[0], edge[1]]["weight"]
            if w == minimal_flow:
                DGf.remove_edge(edge[0], edge[1])
            elif w > minimal_flow:
                DGf.edges[edge[0], edge[1]]["weight"] -= minimal_flow
            DGf.add_edge(edge[1], edge[0], weight=minimal_flow)
        #
        max_flow += minimal_flow
        weight_path = DiGraphDijkstra(DGf, s, t)
    return max_flow


if __name__ == "__main__":
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
    # ShowGraph(DWG_maxflow)
    print(DiGraphMaxiumFlow(DWG_maxflow))
