# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        q1 = [p]
        q2 = [q]

        while q1 and q2:
            cur1 = q1.pop(0)
            cur2 = q2.pop(0)

            if not cur1 and not cur2:
                continue
            if not cur1 or not cur2 or cur1.val != cur2.val:
                return False

            q1.append(cur1.left)
            q1.append(cur1.right)
            q2.append(cur2.left)
            q2.append(cur2.right)
        
        return len(q1) == len(q2)
