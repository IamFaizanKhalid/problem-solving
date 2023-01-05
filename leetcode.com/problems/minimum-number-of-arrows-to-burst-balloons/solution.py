class Solution:
	def findMinArrowShots(self, points: List[List[int]]) -> int:
		points.sort(key=lambda x: x[0])

		count = 0
		pos = float('-inf')

		for point in points:
			if pos < point[0]:
				count+=1
				pos = point[1]
			else:
				pos = min(pos, point[1])

		return count
