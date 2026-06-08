import networkx
from matplotlib import pyplot as plt


def Str2Graph(s: str, directed: bool = False, weight: bool = False) -> networkx.DiGraph:
    """
    parse something like this (DWG):
    A B 10
    A C 20
    B D 30
    B E 40
    C F 50
    C G 60
    """
    if not s:
        return None
    if directed and weight:
        DWG = networkx.DiGraph()
        for line in s.splitlines():
            if not line.strip():
                continue
            src, dst, weight = line.split()
            DWG.add_edge(src.strip(), dst.strip(), weight=int(weight))
        return DWG
    elif directed:
        DG = networkx.DiGraph()
        for line in s.splitlines():
            if not line.strip():
                continue
            src, dst = line.split()
            DG.add_edge(src.strip(), dst.strip())
        return DG
    elif weight:
        G = networkx.Graph()
        for line in s.splitlines():
            if not line.strip():
                continue
            src, dst, weight = line.split()
            G.add_edge(src.strip(), dst.strip(), weight=int(weight))
        return G
    else:
        G = networkx.Graph()
        for line in s.splitlines():
            if not line.strip():
                continue
            src, dst = line.split()
            G.add_edge(src.strip(), dst.strip())
        return G
    return DG


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


if __name__ == "__main__":
    A = Str2Graph(
        """
A B 10
A C 20
B D 30
B E 40
C F 50
C G 60
                """,
        directed=True,
        weight=True,
    )
    PrintGraph(A, weight=True)
    #
    G = networkx.Graph()
    G.add_edges_from(
        [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("C", "G")]
    )
    PrintGraph(G)
    #
    DG = networkx.DiGraph()
    DG.add_edges_from(
        [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("C", "G")]
    )
    PrintGraph(DG)
    #
    WG = networkx.DiGraph()
    WG.add_edges_from(
        [
            ("A", "B", {"weight": 10}),
            ("A", "C", {"weight": 20}),
            ("B", "D", {"weight": 30}),
            ("B", "E", {"weight": 40}),
            ("C", "F", {"weight": 50}),
            ("C", "G", {"weight": 60}),
        ]
    )
    PrintGraph(WG, weight=True)
    #
    #连通性判定
    print(networkx.is_connected(G))#无向图
    print(networkx.is_strongly_connected(DG))#有向图
    #图的度
    G1=networkx.Graph()
    G1.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
    PrintGraph(G1)
    print(G1.degree('A'))#无向图
    DG1=networkx.DiGraph()
    DG1.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
    PrintGraph(DG1)
    print(DG1.in_degree('A'))#有向图入度
    print(DG1.out_degree('A'))#有向图出度
    #networkx建立完全图
    G_complete=networkx.complete_graph(5)
    PrintGraph(G_complete)
    #networkx取得所有简单路径
    for path in networkx.all_simple_paths(G_complete, source=0, target=4):
        print(path)
    #networkx演示邻接矩阵
    G_adj=networkx.Graph()
    G_adj.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')])
    PrintGraph(G_adj)
    adj_matrix=networkx.adjacency_matrix(G_adj,nodelist=['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    print(adj_matrix.todense())
    #
    def TopoSort(G:networkx.DiGraph)->list:
        nodes=list(G.nodes())
        L=[]
        while nodes:
            for node in nodes:
                if G.in_degree(node)==0:
                    L.append(node)
                    nodes.remove(node)
                    break
                else:                
                    raise networkx.NetworkXError("Graph has a cycle, topological sort not possible.")
        return L
