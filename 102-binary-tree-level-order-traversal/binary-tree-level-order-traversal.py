# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        levels = [[root.val]]
        lvl_idx = 0

        queue = [root]

        while queue:
            lvl_size = len(queue)
            level_nodes = []

            for _ in range(lvl_size):
                cur = queue.pop(0)

                if cur.left:
                    queue.append(cur.left)
                    level_nodes.append(cur.left.val)
                if cur.right:
                    queue.append(cur.right)
                    level_nodes.append(cur.right.val)
            
            if level_nodes:
                levels.append(level_nodes)

        return levels

            


        