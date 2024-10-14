class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_length = len(board)

        # Check each row
        for i in range(9):
            seen_tiles = set()

            for j in range(9):
                tile = board[i][j]

                if tile != ".":
                    tile = int(tile)

                    if tile < 1 or tile > 9:
                        return False
                    elif tile in seen_tiles:
                        return False
                    
                    seen_tiles.add(tile)
        
        # Check each column
        for i in range(9):
            seen_tiles = set()

            for j in range(9):
                tile = board[j][i]

                if tile != ".":
                    tile = int(tile)

                    if tile < 1 or tile > 9:
                        return False
                    elif tile in seen_tiles:
                        return False
                    
                    seen_tiles.add(tile)

        # Check each 3x3 subgrid
        for box_y in range(0, 9, 3):  # Iterate over 3x3 subgrid rows
            for box_x in range(0, 9, 3):  # Iterate over 3x3 subgrid columns
                seen_tiles = set()

                for y in range(3):  # Subgrid rows
                    for x in range(3):  # Subgrid columns
                        tile = board[box_y + y][box_x + x]

                        if tile != ".":
                            tile = int(tile)
                            
                            if tile < 1 or tile > 9:
                                return False
                            if tile in seen_tiles:
                                return False

                            seen_tiles.add(tile)
        
        return True