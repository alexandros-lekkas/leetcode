# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def checkH(node):
            if not node:
                return 0

            leftH = checkH(node.left)
            if leftH == -1:
                return -1
            
            rightH = checkH(node.right)
            if rightH == -1:
                return -1

            if abs(leftH - rightH) > 1:
                return -1
            
            return max(leftH, rightH) + 1

        return checkH(root) != -1
        

        

        

        