import networkx
from matplotlib import pyplot as plt


def PrintGraph(
    DWG: networkx.DiGraph | networkx.Graph, weight: bool = False
):
    pos = networkx.circular_layout(DWG)
    networkx.draw_networkx_nodes(DWG, pos=pos)
    networkx.draw_networkx_edges(DWG, pos=pos,connectionstyle="arc3, rad=0.25")
    networkx.draw_networkx_labels(DWG, pos=pos)
    if weight:
        weight_labels = networkx.get_edge_attributes(DWG, "weight")
        networkx.draw_networkx_edge_labels(
            DWG, pos=pos, edge_labels=weight_labels
        )
    plt.show()
    return