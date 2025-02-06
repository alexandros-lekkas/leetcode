# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        q_left = [root.left]
        q_right = [root.right]

        while q_left and q_right:
            cur_left = q_left.pop(0)
            cur_right = q_right.pop(0)

            if not cur_left and not cur_right:
                continue
            if not cur_left or not cur_right or cur_left.val != cur_right.val:
                return False
            
            q_left.append(cur_left.left)
            q_left.append(cur_left.right)

            q_right.append(cur_right.right)
            q_right.append(cur_right.left)
        
        return len(q_left) == len(q_right)
        