class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return(self._valid_row(board) and self._valid_col(board) and self._valid_blob(board))
        
    def _valid_row(self, board: List[List[str]]) -> bool:
        for row in board:
            hash_set = set()
            for num in row:
                if num == ".":
                    continue
                if num in hash_set:
                    return False
                hash_set.add(num)
        return True
    
    def _valid_col(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            hash_set = set()
            for j in range(len(board)):
                val = board[j][i]
                if val == ".":
                    continue
                if val in hash_set:
                    return False
                hash_set.add(val)
        return True
    
    def _valid_blob(self, board: List[List[str]]) -> bool:
        for box_row in range(3):
            for box_col in range(3):
                hash_set = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row * 3 + i][box_col * 3 + j]
                        if val == ".":
                            continue
                        if val in hash_set:
                            return False
                        hash_set.add(val)
        return True
        