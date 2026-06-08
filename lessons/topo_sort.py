import copy
import networkx


def TopoSort(G: networkx.DiGraph) -> list:
    G_test=copy.deepcopy(G)
    L = []
    while G_test.nodes():
        sort_sucess = False
        for node in G_test.nodes():
            if G_test.in_degree(node) == 0:
                L.append(node)
                G_test.remove_node(node)
                sort_sucess = True
                break
        if not sort_sucess:
            raise networkx.NetworkXError(
                "Graph has a cycle, topological sort not possible."
            )
    return L


if __name__ == "__main__":
    DG1 = networkx.DiGraph()
    DG1.add_edges_from(
        [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("C", "G")]
    )
    print(TopoSort(DG1))
    #使用networkx内置的拓扑排序函数
    print("networkx内置的拓扑排序函数：", list(networkx.topological_sort(DG1)))