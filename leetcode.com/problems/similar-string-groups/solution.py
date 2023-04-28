class Solution:
	def numSimilarGroups(self, strs: List[str]) -> int:
		n = len(strs)

		def isSimilar(a,b):
			diff = sum ( a[i] != b[i] for i in range(len(a)) )

			return diff == 0 or diff == 2

		adj = defaultdict(list)
		for i in range(n):
			for j in range(i+1, n):
				if isSimilar(strs[i], strs[j]):
					adj[i].append(j)
					adj[j].append(i)



		visited = [False for _ in range(n)]

		def recurse(node):
			visited[node] = True

			for neighbor in adj[node]:
				if not visited[neighbor]:
					recurse(neighbor)



		count = 0
		for i in range(n):
			if not visited[i]:
				recurse(i)
				count+=1

		return count
