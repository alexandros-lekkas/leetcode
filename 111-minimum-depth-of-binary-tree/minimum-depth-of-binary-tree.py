# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def minD(node, depth):
            result = []

            if not node.left and not node.right:
                return depth + 1
            else:
                if node.left:
                    result.append(minD(node.left, depth + 1))
                if node.right:
                    result.append(minD(node.right, depth + 1))

            return min(result)
        
        return minD(root, 0)