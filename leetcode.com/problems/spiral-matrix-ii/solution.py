class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[-1 for _ in range(n)] for _ in range(n)]

        i,j=0,0
        cur = 1
        last = n*n
        while cur<=last:
            while j<n and ans[i][j] == -1:
                ans[i][j] = cur
                cur += 1
                j += 1
            
            j -= 1
            i += 1

            while i<n and ans[i][j] == -1:
                ans[i][j] = cur
                cur += 1
                i += 1
                
            i -= 1
            j -= 1

            while j>=0 and ans[i][j] == -1:
                ans[i][j] = cur
                cur += 1
                j -= 1

            j += 1
            i -= 1
              
            while i>=0 and ans[i][j] == -1:
                ans[i][j] = cur
                cur += 1
                i -= 1

            i += 1
            j += 1
                

        return ans
