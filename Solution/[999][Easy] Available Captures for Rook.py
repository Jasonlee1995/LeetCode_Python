class Solution:
    def numRookCaptures(self, board):
        r, c = next((i, j) for j in range(8) for i in range(8) if board[i][j] == 'R')
        row = ''.join(board[r][i] for i in range(8) if board[r][i] != '.')
        col = ''.join(board[i][c] for i in range(8) if board[i][c] != '.')
        
        answer = sum(rp in rc for rp in ['Rp', 'pR'] for rc in [row, col])
        return answer