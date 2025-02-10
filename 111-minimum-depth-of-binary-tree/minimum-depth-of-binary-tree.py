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

        q = [[root]]
        dist = 0

        while q:
            cur = q.pop(0)
            dist += 1
            nxt = []

            for node in cur:
                if node:
                    if not node.left and not node.right:
                        return dist
                    else:
                        nxt.append(node.left)
                        nxt.append(node.right)
            
            q.append(nxt)