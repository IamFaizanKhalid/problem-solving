class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2,1), (1,2), (-2,1), (-1,2), (2,-1), (1,-2), (-2,-1), (-1,-2)]

        on_board = lambda r,c: 0<=r<n and 0<=c<n

        @cache
        def recurse(r, c, k):
            if not on_board(r,c):
                return 0

            if k == 0:
                return 1

            total = 0
            for i, j in moves:
                total += recurse(r+i, c+j, k-1)

            return total/8
        
        return recurse(row, column, k)
