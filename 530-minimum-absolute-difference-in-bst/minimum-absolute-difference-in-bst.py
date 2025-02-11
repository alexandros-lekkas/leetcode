# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.prev = float("inf")
        self.answer = float("inf")

    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def minDif(node):
            if node.left:
                minDif(node.left)
            
            self.answer = min(self.answer, abs(node.val - self.prev))
            self.prev = node.val
            
            if node.right:
                minDif(node.right)

        minDif(root)
        return self.answer
        