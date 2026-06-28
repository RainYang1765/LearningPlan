import matplotlib.pyplot as plt
import networkx, copy
from netgraph import Graph
from collections import deque


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

def Kruskal(G:networkx.Graph):
        
    return

if __name__=="__main__":
    pass