class Solution:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		n = len(intervals)

		i = 0
		break1 = False
		while i < n:
			if newInterval[1] < intervals[i][0]: 
				break
			elif newInterval[0] <= intervals[i][1]:
				break1 = True
				break
			i += 1

		start = i

		break2 = False
		while i < n:
			if newInterval[1] < intervals[i][0]: 
				break
			elif newInterval[1] <= intervals[i][1]:
				break2 = True
				break
			i += 1

		end = i


		# print(start, end)
		# print(break1, break2)

		x = intervals[:start]
		z = intervals[end+1:] if break2 else intervals[end:]

		y = [[\
		min(intervals[start][0], newInterval[0]) if break1 else newInterval[0], \
		max(intervals[end][1], newInterval[1]) if break2 else newInterval[1] \
		]]

		# print(x,y,z)

		return x + y + z
