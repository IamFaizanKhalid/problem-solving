class Solution:
	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
		rows = {}
		for i, row in enumerate(mat):
			rows[i]=sum(row)

		weak = []
		for i,s in sorted(rows.items(), key=lambda item: item[1]):
			weak.append(i)

		return weak[:k]
