class Solution:
	def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # union find
		group = [i for i in range(n)]

		def find(x: int) -> int:
			if group[x] == x:
				return x

			group[x] = find(group[x]) 
			return group[x]

		def union(x: int, y: int) -> None:
			x = find(x)
			y = find(y)

			if x < y:
				group[y] = x
			elif x > y:
				group[x] = y

		def sameGroup(x: int, y: int) -> bool:
			return find(x) == find(y)



        # sorting quries by limits
		n = len(queries)
		
		for i in range(n):
			queries[i].append(i) # remember original index
		
		queries.sort(key=lambda x: x[2]) # by limit
		
		answer = [False for _ in range(n)]
		

        # sorting edges by distance
		n = len(edgeList)

		edgeList.sort(key=lambda x: x[2]) # by distance

        # start from min dis and limit
		i = 0
		for p,q,limit,qi in queries:
			while i<n:
				u, v, dis = edgeList[i]
				if dis>=limit:
					break
				union(u, v)
				i+=1

            # connected using edges with dis in limit
			answer[qi] = sameGroup(p, q)

		return answer
