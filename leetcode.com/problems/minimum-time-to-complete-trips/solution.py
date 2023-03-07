class Solution:
	def minimumTime(self, time: List[int], totalTrips: int) -> int:

		def isTimeEnough(t):
			trips = 0
			for busTime in time:
				trips += t // busTime
			return trips >= totalTrips
		
		minT = 1
		maxT = max(time) * totalTrips

		while minT < maxT:
			t = (minT + maxT) // 2
			if isTimeEnough(t):
				maxT = t
			else:
				minT = t + 1

		return minT
