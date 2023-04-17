class Solution:
	def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
		required = max(candies) - extraCandies

		return [count >= required for count in candies]
