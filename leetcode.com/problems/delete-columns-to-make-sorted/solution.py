class Solution:
	def minDeletionSize(self, strs: List[str]) -> int:
		l = len(strs[0])

		toRemoveCount = 0

		for c in range(l):
			x = strs[0][c]
			for i in range(len(strs)):
				if strs[i][c] < x:
					toRemoveCount += 1
					break
				x = strs[i][c]

		return toRemoveCount
