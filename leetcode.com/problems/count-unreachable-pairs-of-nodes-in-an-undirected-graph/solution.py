class Solution:
	def countPairs(self, n: int, edges: List[List[int]]) -> int:

		paths = defaultdict(list)
		for a,b in edges:
			paths[a].append(b)
			paths[b].append(a)

		visited = [False for _ in range(n)]
		
		def recurse(i):
			if visited[i]:
				return 0

			visited[i] = True

			total = 1
			for adj in paths[i]:
				total += recurse(adj)
			
			return total


		answer = 0 
		remaining = n	
		for i in range(n):
			if not visited[i]:
				count = recurse(i)
				remaining -= count
				answer += count * remaining
	  
		return answer
