class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        sum_upto = lambda n: (n*(n+1))//2

        def getSum(n, mx):
            sm = sum_upto(mx)
            if mx < n:
                sm += n-mx # add ones
            elif mx > n:
                sm -= sum_upto(mx-n) # subtract extra

            return sm
            

        def getGuessSum(guess):
            left = getSum(index, guess-1)
            right = getSum(n-index-1, guess-1)

            # print(guess,left,right)

            return guess + left + right

        
        l,r = 1,maxSum
        while l<r:
            guess = (l+r+1) // 2
            
            if getGuessSum(guess) <= maxSum:
                l = guess
            else:
                r = guess-1
        
        return l
