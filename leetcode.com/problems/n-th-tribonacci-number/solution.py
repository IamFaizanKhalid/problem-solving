class Solution:
	def __init__(self):
		self.dp = [0,1,1]+[-1 for _ in range(3,38)]
		
	def tribonacci(self, n: int) -> int:
		if self.dp[n] == - 1:
			self.dp[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

		return self.dp[n]
