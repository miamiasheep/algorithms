# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        level = [root]
        while root and level:
            ans.append([i.val for i in level])
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return ans
    
    
