class Solution:
	def countOdds(self, low: int, high: int) -> int:
		# 3 4 5 6 
		# 8 9 10
		rng = high-low
		return low%2 + rng//2 + rng%2 * (1 - low%2)
		# if low%2==0:
		#	 return rng//2 + rng%2
		# else:
		#	 return 1 + rng//2
    
