# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def helper(node, prevVals, targetSum):

            if not node:
                return False
            curPathVal = prevVals + node.val
            if not node.left and not node.right:
                if curPathVal == targetSum:
                    return True
            else:
                if helper(node.left, curPathVal, targetSum):
                    return True
                elif helper(node.right, curPathVal, targetSum):
                    return True

            return False 

        return helper(root, 0, targetSum)
        