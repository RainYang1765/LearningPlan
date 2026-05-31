class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Str2Tree(istr:str)->TreeNode:
    #pattern as {1,#,2,3}
    #2^n - 1 < 节点总数 < 2^(n+1) - 1
    node_list = istr[1:-1].split(',')
    if not node_list:
        return None
    root = TreeNode(int(node_list[0]))
    queue = [root]
    i = 1
    while queue and i < len(node_list):
        node = queue.pop(0)
        if node:
            if node_list[i] != '#':
                node.left = TreeNode(int(node_list[i]))
                queue.append(node.left)
            i += 1
            if i < len(node_list) and node_list[i] != '#':
                node.right = TreeNode(int(node_list[i]))
                queue.append(node.right)
            i += 1
    return root

def PrintTree(root:TreeNode):
    if not root:
        print('#', end=' ')
        return
    print(root.val, end=' ')
    PrintTree(root.left)
    PrintTree(root.right)

def BFSTree(root:TreeNode):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            print(node.val, end=' ')
            queue.append(node.left)
            queue.append(node.right)
        else:
            print('#', end=' ')

def DFSTree(root:TreeNode):
    if not root:
        print('#', end=' ')
        return
    print(root.val, end=' ')
    DFSTree(root.left)
    DFSTree(root.right)

if __name__ == '__main__':
    tree_str = '{1,2,3,4,#,6,7,#,9}'
    root = Str2Tree(tree_str)
    BFSTree(root)
