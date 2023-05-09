class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        ans = []

        i,j=0,0
        count = n*m
        while count:
            while j<n and not visited[i][j]:
                visited[i][j] = True
                count -= 1
                ans.append(matrix[i][j])
                j += 1
            
            j -= 1
            i += 1

            while i<m and not visited[i][j]:
                visited[i][j] = True
                count -= 1
                ans.append(matrix[i][j])
                i += 1
                
            i -= 1
            j -= 1

            while j>=0 and not visited[i][j]:
                visited[i][j] = True
                count -= 1
                ans.append(matrix[i][j])
                j -= 1

            j += 1
            i -= 1
              
            while i>=0 and not visited[i][j]:
                visited[i][j] = True
                count -= 1
                ans.append(matrix[i][j])
                i -= 1

            i += 1
            j += 1
                

        return ans
