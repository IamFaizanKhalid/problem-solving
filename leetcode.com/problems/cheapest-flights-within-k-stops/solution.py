class Solution:
	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
		adjacents = defaultdict(lambda: [])
		for f, t, cost in flights:
			adjacents[f].append((t,cost))
	
		minCost = [float('inf') for _ in range(n)]

		queue = deque([(src, 0)])
		kc = 0

		while queue and kc <= k:
			batch = len(queue)
			# loop on the same level
			for i in range(batch):
				cur, cost = queue.popleft()
				for adj, ticket in adjacents[cur]:
					if cost + ticket < minCost[adj]:
						minCost[adj] = cost + ticket
						queue.append((adj, minCost[adj]))
			kc += 1

		return -1 if minCost[dst] == float('inf') else minCost[dst]
