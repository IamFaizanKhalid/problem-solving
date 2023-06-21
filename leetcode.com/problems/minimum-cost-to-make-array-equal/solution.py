class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)

        def get_total(tgt):
            total = 0
            for i in range(n):
                total += cost[i] * abs(tgt-nums[i])
    
            return total
        
        l, r = min(nums), max(nums)

        mn = get_total(nums[0])
        
        while l < r:
            m = (l + r) // 2
            total1 = get_total(m)
            total2 = get_total(m+1)

            mn = min(total1, total2)
            
            if total1 > total2:
                l = m + 1
            else:
                r = m
        
        return mn
