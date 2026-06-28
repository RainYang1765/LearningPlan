import networkx


def IsDoubleConnected(G: networkx.Graph):
    def _dfs(G: networkx.Graph, visit: dict, num: dict, low: dict, start):
        if start and not visit[start]:
            visit[start] = True
            nonlocal counter
            counter += 1
            num[start] = counter
            low[start] = counter
            print(f"Node : {start} Num : {num[start]}")
            for node in G.neighbors(start):
                if not visit[node]:  # 遍历前向边
                    prev[node] = start
                    _dfs(G, visit, num, low, node)
                    if low[node] >= num[start]:
                        print(f"Articular node : {start}")
                    low[start] = min(low[start], low[node])
                    print(f"Low update - forward : {low[start]} node : {start}")
                elif prev[start] != node:  # 跳过前向边
                    low[start] = min(low[start], num[node])
                    print(f"Low update - backward : {low[start]} node : {start}")

    #
    counter = 0
    visit = {}
    num = {}
    low = {}
    prev = {}
    for node in G.nodes:
        visit[node] = False
        num[node] = None
        low[node] = None
        prev[node] = None
    for node in G.nodes:
        if not visit[node]:
            _dfs(G, visit, num, low, node)
    counter = 0
    #
    return


def Tarjan(G: networkx.Graph):
    counter = 0
    root=None
    root_childs=0

    def FindArt(G: networkx.Graph, v, visit: dict, low: dict, num: dict, parent: dict):
        nonlocal counter
        nonlocal root
        nonlocal root_childs
        
        visit[v] = True
        counter += 1
        low[v] = counter
        num[v] = counter
        for w in G.neighbors(v):
            if not visit[w]:
                parent[w] = v
                if v==root:
                    root_childs+=1
                FindArt(G, w, visit, low, num, parent)
                if low[w] >= num[v]:
                    print(f"{v} is an articulation point!")
                low[v] = min(low[v], low[w])
            elif parent[v] != w:
                low[v] = min(low[v], num[w])

    visit={}
    low={}
    num={}
    parent={}
    for node in G.nodes():
        visit[node]=False
        low[node]=float("inf")
        num[node]=float("inf")
        parent[node]=None
    for node in G.nodes():
        if not visit[node]:
            print("ENCOUNTER!")
            root=node
            root_childs=0
            FindArt(G,node,visit,low,num,parent)
            if root_childs>1:
                print(f"root {root} is articulation points!")
            else:
                print(f"root {root} is not articulation points!")

if __name__ == "__main__":
    # alist = [
    #     (4, 5, 2),
    #     (1, 3, 0),
    #     (1, 4, 1),
    #     (2, 1, 1),
    #     (4, 1, 0),
    #     (2, 4, 0),
    #     (4, 3, 0),
    # ]
    # alist.sort(key=lambda x: x[2])
    # for edge in alist:
    #     print(edge)
    # exit()
    G = networkx.Graph()
    G.add_edges_from(
        [
            ("B", "A"),
            ("B", "C"),
            ("A", "D"),
            ("C", "D"),
            ("D", "E"),
            ("D", "F"),
            ("E", "F"),
            ("C", "G"),
        ]
    )
    # IsDoubleConnected(G)
    Tarjan(G)
    print(f"Articulation points from networkx {list(networkx.articulation_points(G))}")
