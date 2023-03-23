class Solution:
	def makeConnected(self, n: int, connections: List[List[int]]) -> int:
		if len(connections) < n - 1:
			return -1

		paths = defaultdict(list)

		for connection in connections:
			paths[connection[0]].append(connection[1])
			paths[connection[1]].append(connection[0])

		visited = [False for _ in range(n)]

		def traverse(node):
			visited[node] = True

			for adj in paths[node]:
				if not visited[adj]:
					traverse(adj)

		nonConnectedGraphs = 0
		for i in range(n):
			if not visited[i]:
				nonConnectedGraphs += 1
				traverse(i)

		return nonConnectedGraphs - 1
	
