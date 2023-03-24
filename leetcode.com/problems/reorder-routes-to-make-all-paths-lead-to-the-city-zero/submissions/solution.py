class Solution:
	def minReorder(self, n: int, connections: List[List[int]]) -> int:
		paths = defaultdict(list)

		for a,b in connections:
			paths[a].append((b, True))
			paths[b].append((a, False))

		visited = [False for _ in range(n)]

		count = 0

		q = [0] # bfs
		while q:
			city = q.pop()

			for adj, fwd in paths[city]:
				if not visited[adj]:
					visited[city] = True
					if fwd:
						count += 1
					q.append(adj)

		return count
	
