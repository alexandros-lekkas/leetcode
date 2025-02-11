class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        per = 0
        rows = len(grid)
        columns = len(grid[0])

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    if ((i > 0) and (grid[i - 1][j] == 0)) or (i == 0):
                        per += 1

                    if ((j > 0) and (grid[i][j - 1] == 0)) or (j == 0):
                        per += 1

                    if ((i < rows - 1) and (grid[i + 1][j] == 0)) or (i == rows - 1):
                        per += 1

                    if ((j < columns - 1) and (grid[i][j + 1] == 0)) or (j == columns - 1):
                        per += 1

        return per