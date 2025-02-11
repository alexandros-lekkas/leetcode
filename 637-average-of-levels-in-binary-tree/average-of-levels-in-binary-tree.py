# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root:
            return []

        queue = [[root]]
        result = []

        while queue:
            current = queue.pop(0)

            level_sum = 0
            level_count = len(current)

            level = []
            for node in current:
                level_sum += node.val

                if node.left: level.append(node.left)
                if node.right: level.append(node.right)

            if level:
                queue.append(level)
            result.append(level_sum / float(level_count))
        
        return result

        