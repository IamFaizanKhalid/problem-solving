class Solution:
	def findJudge(self, n: int, trust: List[List[int]]) -> int:
		trustOn = [0 for _ in range(n+1)]
		trustBy = [0 for _ in range(n+1)]

		for a,b in trust:
			trustBy[a] += 1
			trustOn[b] += 1

		for i in range(1, n+1):
			if trustOn[i] == n-1 and trustBy[i] == 0:
				return i

		return -1
