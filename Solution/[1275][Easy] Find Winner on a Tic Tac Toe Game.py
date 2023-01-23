class Solution:
    def tictactoe(self, moves):
        n = 3
        row, col = [[0] * n for _ in range(2)]
        dig = [0] * 2
        move = [1, -1]
        for i, (r, c) in enumerate(moves):
            m = move[i%2]
            row[r] += m
            col[c] += m

            if (r, c) in [(0, 0), (1, 1), (2, 2)]:
                dig[0] += m
            if (r, c) in [(0, 2), (1, 1), (2, 0)]:
                dig[1] += m
            
            for rcd in [row, col, dig]:
                if m * n in rcd:
                    return 'AB'[i%2]
        
        if len(moves) < n ** 2: return 'Pending'
        return 'Draw'