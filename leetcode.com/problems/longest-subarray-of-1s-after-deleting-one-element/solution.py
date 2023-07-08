class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        sLast0 = -1
        last0 = -1

        mx = 0
        for i in range(n):
            if nums[i] == 0:
                if last0 != -1:
                    mx = max(mx, i-sLast0-2)

                sLast0 = last0
                last0 = i

        if sLast0 == -1:
            return n-1

        if last0 != -1:
            mx = max(mx, n-sLast0-2)

        return mx        
