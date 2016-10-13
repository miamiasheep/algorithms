# This class is a binary tree
# which support tree-related question in leetcode
class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# print tree using level_order_traversal
def level_order_traversal(root):
    ans = []
    level = [root]
    while root and level:
        ans.append([i.val for i in level])
        level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
    print ans

if __name__ == '__main__':
    tree = Tree(1)
    tree.left = Tree(2)
    tree.right = Tree(3)
    tree.left.left = Tree(4)
    
    level_order_traversal(tree)
    
        