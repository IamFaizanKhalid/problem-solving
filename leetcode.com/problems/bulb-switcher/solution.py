class Solution:
	def bulbSwitch(self, n: int) -> int:
		# return math.floor(math.log2(n)) if n>1 else n
		return int(math.sqrt(n))
