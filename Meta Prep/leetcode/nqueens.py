def solveNQueens(self, n: int):
    cols = set()
    diag = set() # row - col
    anti_diag = set() # row + col
    results = []
    
    board = [["." * n for _ in range(n)]]
    
    def backtrack(row: int) -> None:
        if row == n:
            results.append(["".join(r) for r in board])
            return 
        
        for col in range(n):
            if col in cols or (row-col) in diag or (row+col) in anti_diag:
                continue 
            
            #place queen
            board[row][col] = "Q"
            cols.add(col)
            diag.add(row-col)
            anti_diag.add(row+col)
            
            backtrack(row+1)
            
            board[row][col] = "."
            cols.remove(col)
            diag.remove(row-col)
            anti_diag.remove(row+col)
        
    backtrack(0)
    return results
    
            
            
            
    
    