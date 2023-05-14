class Solution:
    def maxScore(self, nums: List[int]) -> int:

        n = len(nums)

        isOn = lambda num, n: (num>>n)&1 == 1
        turnOn = lambda num, n: num|(1<<n)

        possiblePairs = 2**n
        dp = [-1 for _ in range(possiblePairs)]

        def backtrack(selected, op):
            if op > n//2:
                return 0

            if dp[selected]==-1:
                mx = 0
                for i in range(n):
                    for j in range(i+1, n):

                        if isOn(selected,i) or isOn(selected,j):
                            continue

                        addedSelection = turnOn(selected, i)
                        addedSelection = turnOn(addedSelection, j)

                        score = op * math.gcd(nums[i],nums[j]) + backtrack(addedSelection, op+1)

                        mx = max(mx, score)
                        
                dp[selected] = mx


            return dp[selected]

        
        return backtrack(0,1)
    
