class Solution:
	def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
		paths = {}

		for edge in edges:
			if edge[0] in paths:
				paths[edge[0]].append(edge[1])
			else:
				paths[edge[0]] = [edge[1]]

			if edge[1] in paths:
				paths[edge[1]].append(edge[0])
			else:
				paths[edge[1]] = [edge[0]]

		# print(paths)

		visited = [False for x in range(n)]
		result = [0 for x in range(n)]

		def dfs(cur):
			count = {}

			if visited[cur]:
				return count

			visited[cur] = True

			if cur in paths:
				for child in paths[cur]:
					nc = dfs(child)
					count = {c: count.get(c, 0) + nc.get(c, 0) for c in set(count) | set(nc)}

			visited[cur] = False

			lbl=labels[cur]

			if lbl in count:
				count[lbl] +=1
			else:
				count[lbl] = 1
			
			result[cur] = count[lbl]

			# print(cur,count)

			return count

		dfs(0)

		return result
