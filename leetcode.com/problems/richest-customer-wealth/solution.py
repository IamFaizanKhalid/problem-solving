class Solution:
	def maximumWealth(self, accounts: List[List[int]]) -> int:
		max = 0
		for person in accounts:
			s = sum(person)
			if s > max:
				max = s
		return max
