class Solution:
	def zeroFilledSubarray(self, nums: List[int]) -> int:
		ss = lambda n: n*(n+1)//2

		total = 0
		chunk = 0
		for num in nums:
			if num == 0:
				chunk += 1
			else:
				total += ss(chunk)
				chunk = 0

		return total + ss(chunk)
