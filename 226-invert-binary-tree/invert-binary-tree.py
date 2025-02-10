# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        
        def invert(node):
            left = node.left
            node.left = node.right
            node.right = left

            if node.left: invert(node.left)
            if node.right: invert(node.right)

        invert(root)
        return root
        