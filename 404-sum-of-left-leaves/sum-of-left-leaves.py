# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0

        q = [root]
        sum = 0

        while q:
            cur = q.pop(0)

            if cur.left:
                q.append(cur.left)
                if not cur.left.left and not cur.left.right:
                    sum += cur.left.val
            if cur.right:
                q.append(cur.right)
        
        return sum

        