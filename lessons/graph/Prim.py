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


def Prim(G: networkx.Graph):
    dr = {}
    pr = {}
    visit = {}
    L = []
    forest=[]
    for node in G.nodes:
        dr[node] = float("inf")
        pr[node] = None
        visit[node] = False

    def SelectStart(v: dict):
        src = None
        for k, v in visit.items():
            if v == False:
                src = k
                break
        return src

    src = SelectStart(visit)
    #
    while src:
        #
        dr[src] = 0
        L.append(src)
        while L:
            node=None
            min_dr=float("inf")
            for n in L:
                if dr[n]<min_dr:
                    node=n
                    min_dr=dr[n]
            visit[node]=True
            L.remove(node)
            for neighbor in G.neighbors(node):
                if (
                    dr[neighbor] > G.edges[node, neighbor]["weight"]
                    and not visit[neighbor]
                ):
                    dr[neighbor] = G.edges[node, neighbor]["weight"]
                    pr[neighbor] = node
                    L.append(neighbor)
        #
        tree=[]
        for n in G.nodes:
            if n!=src and visit[n]==True:
                tree.append((pr[n],n))
        forest.append(tree)
        #
        src = SelectStart(visit)
    return forest


if __name__ == "__main__":
    pass
