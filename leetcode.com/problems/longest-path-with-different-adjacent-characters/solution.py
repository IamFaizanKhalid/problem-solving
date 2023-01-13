class Solution:
	def longestPath(self, parent: List[int], s: str) -> int:
		if len(s) == 1:
			return 1
		
		if len(s) == 2:
			return 2 if s[0]!=s[1] else 1
		

		paths = {}

		for c, p in enumerate(parent):
			if p == -1:
				continue

			if p in paths:
				paths[p].append(c)
			else:
				paths[p] = [c]
			
			if c in paths:
				paths[c].append(p)
			else:
				paths[c] = [p]

		print(paths)

		visited = [False for _ in s]

		dp = {}

		def recurse(p, gp):
			if visited[p]:
				return 0

			if (p, gp) in dp:
				return dp[(p, gp)]

			visited[p] = True

			mx = 0
			for c in paths[p]:
				if s[c] != s[p]:
					mx = max(mx, recurse(c, p))

			visited[p] = False
			
			dp[(p, gp)] = 1+mx

			return 1+mx

		mx = 0

		for i in range(len(s)):
			mx = max(mx, recurse(i, -1))

		return mx
