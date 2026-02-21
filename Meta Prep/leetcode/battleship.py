class Solution:
    def countBattleships(self,board):
        ships = 0 
        m,n = len(board),len(board[0]) #row,col

        if not board or not board[0]:
            return 0 
        
        for r in range(m):
            for c in range(n):
                if board[r][c] != 'X':
                    continue

                if r > 0 and board[r-1][c] == 'X':
                    continue 

                if c > 0 and board[r][c-1] == 'X':
                    continue 

                ships += 1
        return ships 


        
