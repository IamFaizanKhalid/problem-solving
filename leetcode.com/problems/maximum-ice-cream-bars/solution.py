class Solution:
	def maxIceCream(self, costs: List[int], coins: int) -> int:
		costs.sort()

		ic = 0
		for cost in costs:
			if coins < cost:
				break
			ic += 1
			coins -= cost

		return ic
