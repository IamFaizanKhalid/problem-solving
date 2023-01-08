class Solution:
	def maxPoints(self, points: List[List[int]]) -> int:
		if len(points)<3:
			return len(points)

		max_p = 0
		for i in range(len(points)):
			for j in range(i+1,len(points)):
				p = 0
				if points[j][0]==points[i][0]: # vertical
					for point in points:
						if point[0] == points[i][0]:
							p+=1 
				else:
					m = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
					for point in points:
						if abs((points[i][1]-point[1])-m*(points[i][0]-point[0]))<0.0001:
							p+=1

				max_p = max(max_p,p)

		return max_p
