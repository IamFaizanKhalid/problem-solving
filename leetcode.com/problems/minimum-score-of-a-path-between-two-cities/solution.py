class Solution:
	def minScore(self, n: int, roads: List[List[int]]) -> int:
		scores = {}
		paths = defaultdict(list)

		for a,b,dist in roads:
			paths[a].append(b)
			paths[b].append(a)
			scores[(a,b)]=dist
			scores[(b,a)]=dist

		visited = [False for _ in range(n+1)]
		visited[1] = True

		score = float('inf')
		q = [1]

		while q:
			city = q.pop()
			for adj in paths[city]:
				# before if because we can go and come back this path
				score = min(score, scores[(city,adj)])
				if not visited[adj]:
					visited[adj] = True
					q.append(adj)

		return score
