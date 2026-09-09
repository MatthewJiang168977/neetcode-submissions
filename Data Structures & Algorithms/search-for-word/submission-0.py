class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(curr_look, row, col): 
            if curr_look == len(word): 
                return True 
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) \
            or board[row][col] != word[curr_look]: 
                return False 
            else: 
                temp = board[row][col]
                board[row][col] = "#"
                result = \
                dfs(curr_look+1, row-1, col) or \
                dfs(curr_look+1, row+1, col) or \
                dfs(curr_look+1, row, col+1) or \
                dfs(curr_look+1, row, col-1)
                board[row][col] = temp 
                return result 

        for r in range(len(board)):
            for c in range(len(board[0])): 
                if dfs(0,r,c): 
                    return True 
        return False 


