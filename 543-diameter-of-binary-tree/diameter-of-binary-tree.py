# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxDiameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            self.maxDiameter = max(self.maxDiameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1
        
        dfs(root)
        return self.maxDiameter
