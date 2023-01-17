class Solution:
	def minFlipsMonoIncr(self, s: str) -> int:
		flips = 0
		onesCount = 0

		# for string upto c
		for c in s:
			if c == '1':
				# 1 at the end, string is still monotone
				onesCount += 1
			else:
				# flip this last 0 to 1 to make string monotone
				# flips += 1
				# or we can flips all 1s before this to 0 to make it monotone
				# flips = onesCount
				# we will choose minimum flips
				flips = min(onesCount, flips + 1)

		return flips
