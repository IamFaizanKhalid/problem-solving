class Solution:
	def maxPoints(self, points: List[List[int]]) -> int:
		if len(points)<3:
			return len(points)

		# for points pa and pb:
		#  m=(pb[y]-pa[y])/(pb[x]-pa[x])
		#
		# for a points p on the same line:
		# https://math.stackexchange.com/a/637926
		#	 (p[y]-pa[y]) / (p[x]-pa[x]) = (pb[y]-pa[y]) / (pb[x]-pa[x])
		#  => (pa[y]-pb[y])*p[x] - (pa[x]-pb[x])*p[y] + pa[x]*pb[y] - pb[x]*pa[y] = 0
		#
		# for the known values of pa and pb:
		#	ax + by + c = 0
		#	a = pa[y]-pb[y]
		#	b = pa[x]-pb[x]
		#	c = pa[x]*pb[y] - pb[x]*pa[y]
		#
		#	a*p[x] - b*p[y] + c = 0

		lines = {}

		max_p = 0
		for i,pa in enumerate(points):
			for j in range(i+1,len(points)):
				pb = points[j]

				if i!=j:
					a = pa[1]-pb[1]
					b = pa[0]-pb[0]
					c = pa[0]*pb[1] - pb[0]*pa[1]

					line = (a,b,c)

					if a!=0:
						# (1,2,3), (2,4,6), (-1,-2,-3) all respresent the same line
						# dividing each element by a to get the ratio
						b/=a
						c/=a
						line = (1,b,c)

					elif b!=0:
						# so does (0,-1,-3) and (0,8,24)
						a/=b
						c/=b
						line = (a,1,c)

					# print(line)

					if line not in lines:
						lines[line] = {tuple(pa), tuple(pb)}
					else:
						lines[line].add(tuple(pb))

		# print(lines)
		return len(max(lines.values(), key=len))
