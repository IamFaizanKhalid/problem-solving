class Solution:
	def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
		ufSet = {}

		def find(x):
			ufSet.setdefault(x,x)

			if ufSet[x] != x:
				ufSet[x] = find(ufSet[x])

			return ufSet[x]

		def union(x,y):
			ufSet[find(x)] = find(y)
		

		# geting adjacents of each node and all nodes against each value
		adjacents = defaultdict(list)
		v_nodes = defaultdict(set)
		for s,e in edges:
			adjacents[e].append(s)
			v_nodes[vals[s]].add(s)
			adjacents[s].append(e)
			v_nodes[vals[e]].add(e)
		
		# adding single node paths
		total = len(vals)
		
		for val, nodes in sorted(v_nodes.items()):
			# nodes having the same value (starting from the smallest)
			for node in nodes:
				for adjacent in adjacents[node]:
					if vals[adjacent] <= val:
						union(node, adjacent)

			# counting the number of elements in each set for the current value
			groupCount = defaultdict(int)
			for node in nodes:
				groupCount[find(node)] += 1
				
			# getting possible combinations of size 2 for each group for the current value
			for _, count in groupCount.items():
				total += comb(count, 2)

		return total
