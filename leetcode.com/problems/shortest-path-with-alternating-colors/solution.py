class Solution:
	def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

		rPaths = defaultdict(list)
		for edge in redEdges:
			rPaths[edge[0]].append(edge[1])

		
		bPaths = defaultdict(list)
		for edge in blueEdges:
			bPaths[edge[0]].append(edge[1])

		
		rVisited = [False for _ in range(n)]
		bVisited = [False for _ in range(n)]

		rVisited[0] = True
		bVisited[0] = True

		shortest = [float('inf') for _ in range(n)]
		shortest[0] = 0

		q = deque()

		for adj in rPaths[0]:
			if adj == 0:
				continue
			shortest[adj] = 1
			if not rVisited[adj]:
				q.append((adj, True, 1)) # (node, red, dist)

		for adj in bPaths[0]:
			if adj == 0:
				continue
			shortest[adj] = 1
			if not bVisited[adj]:
				q.append((adj, False, 1)) # (node, red, dist)


		while q:
			node, red, dist = q.popleft()

			if red:
				rVisited[node] = True

				for adj in bPaths[node]:
					shortest[adj] = min(shortest[adj], dist+1)
					if not bVisited[adj]:
						q.append((adj, False, dist+1))
			else:
				bVisited[node] = True
				
				for adj in rPaths[node]:
					shortest[adj] = min(shortest[adj], dist+1)
					if not rVisited[adj]:
						q.append((adj, True, dist+1))

		for i in range(n):
			if shortest[i] == float('inf'):
				shortest[i] = -1

		return shortest
