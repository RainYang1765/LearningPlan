class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def Str2Tree(istr: str) -> TreeNode:
    # pattern as {1,#,2,3}
    # 2^n - 1 < 节点总数 < 2^(n+1) - 1
    node_list = istr[1:-1].split(",")
    if not node_list:
        return None
    root = TreeNode(int(node_list[0]))
    queue = [root]
    i = 1
    while queue and i < len(node_list):
        node = queue.pop(0)
        if node:
            if node_list[i] != "#":
                node.left = TreeNode(int(node_list[i]))
                queue.append(node.left)
            i += 1
            if i < len(node_list) and node_list[i] != "#":
                node.right = TreeNode(int(node_list[i]))
                queue.append(node.right)
            i += 1
    return root


def PrintTree(root: TreeNode):
    if not root:
        print("#", end=" ")
        return
    print(root.val, end=" ")
    PrintTree(root.left)
    PrintTree(root.right)


def BFSTree(root: TreeNode):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            print(node.val, end=" ")
            queue.append(node.left)
            queue.append(node.right)
        else:
            print("#", end=" ")


def DFSTreePreorder(root: TreeNode):
    if root:
        print(root.val, end=" ")
        DFSTreePreorder(root.left)
        DFSTreePreorder(root.right)
    else:
        print("#", end=" ")
    return


def DFSTreeInorder(root: TreeNode):
    if root:
        DFSTreeInorder(root.left)
        print(root.val, end=" ")
        DFSTreeInorder(root.right)
    else:
        print("#", end=" ")
    return


def DFSTreePostorder(root: TreeNode):
    if root:
        DFSTreePostorder(root.left)
        DFSTreePostorder(root.right)
        print(root.val, end=" ")
    else:
        print("#", end=" ")
    return

def MakeMiniheap(root:TreeNode) -> TreeNode:
    if not root:
        return None
    left_min = MakeMiniheap(root.left)
    right_min = MakeMiniheap(root.right)
    if left_min and left_min.val < root.val:
        root.val, left_min.val = left_min.val, root.val
    if right_min and right_min.val < root.val:
        root.val, right_min.val = right_min.val, root.val
    return root

def TopK(a:list[int], k:int) -> list[int]:
    # 维护一个大小为k的最小堆
    import heapq
    if k <= 0:
        return []
    if k > len(a):
        return sorted(a, reverse=True)
    min_heap = []
    for num in a:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
    return sorted(min_heap, reverse=True)


if __name__ == "__main__":
    tree_str = "{1,2,3,4,#,6,7,#,9}"
    root = Str2Tree(tree_str)
    BFSTree(root)
