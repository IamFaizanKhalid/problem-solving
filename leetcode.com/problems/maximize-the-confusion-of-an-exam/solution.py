class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)

        def getMax(c):
            i=0
            mx=0
            
            count=0

            for j in range(n):
                if answerKey[j] != c:
                    count += 1

                while count > k:
                    if answerKey[i] != c:
                        count -= 1
                    i += 1
                    
                mx = max(mx, j-i+1)
                print(i,j)
                                
            return mx


        return max(getMax('T'), getMax('F'))
