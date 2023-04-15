class Solution:
	def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
		n = len(piles)
		
		dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]

		def recurse(i,k):
			if i==0:
				return 0

			if dp[i][k] == -1:
				sm = 0

				for coins in range(0, min(len(piles[i-1]), k)+1):
					if coins > 0:
						sm += piles[i-1][coins-1]
					dp[i][k] = max(dp[i][k], sm+recurse(i-1, k-coins))

			return dp[i][k]

		return recurse(n,k)
