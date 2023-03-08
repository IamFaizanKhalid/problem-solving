class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:

		def timeForK(k):
			t = 0
			for pile in piles:
				t += ceil(pile/k)

			return t

		minK = 1
		maxK = max(piles)

		while minK < maxK:
			k = (minK+maxK)//2

			hk = timeForK(k)

			if hk <= h:
				maxK = k
			else:
				minK = k+1

		return minK
