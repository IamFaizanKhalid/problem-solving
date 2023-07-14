class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)

        mx = 1
        for num in arr:
            dp[num] = dp[num-difference] + 1
            mx = max(mx, dp[num])
            
        return mx
