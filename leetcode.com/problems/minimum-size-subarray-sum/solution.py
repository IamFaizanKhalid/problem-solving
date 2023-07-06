class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        INT_MAX = float('inf')

        i = 0        
        sm = 0

        mn = INT_MAX

        for j in range(n):
            sm += nums[j]

            while sm >= target:
                mn = min(mn, j-i+1)
                sm -= nums[i]
                i += 1


        return mn if mn != INT_MAX else 0
