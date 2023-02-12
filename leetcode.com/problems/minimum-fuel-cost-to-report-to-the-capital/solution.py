class Solution:
	def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
		n = len(roads) + 1

		if n < 3:
			return n-1

		paths = defaultdict(list)
		for road in roads:
			paths[road[0]].append(road[1])
			paths[road[1]].append(road[0])

		visited = [False for _ in range(n)]

		def recurse(node):
			visited[node] = True

			adjPersons = adjLitres = 0
			for adj in paths[node]:
				if not visited[adj]:
					p, l = recurse(adj)
					adjPersons += p
					adjLitres += l

			visited[node] = False

			persons = adjPersons
			litres = adjLitres

			if node != 0:
				persons += 1
				cars = int(ceil(persons / seats))
				litres += cars

			return persons, litres
			
		
		return recurse(0)[1]
		
