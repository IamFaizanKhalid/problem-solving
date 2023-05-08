class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        sm = 0
        for i in range(n):
            sm += mat[i][i] + mat[i][n-1-i]
        
        if n%2 != 0:
            sm -= mat[n//2][n//2]

        return sm
