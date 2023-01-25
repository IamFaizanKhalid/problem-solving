class Solution:
	def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
		n = len(edges)

		d1 = [-1 for _ in range(n)]
		d2 = [-1 for _ in range(n)]

		node = node1
		d = 0
		while node != -1:
			d1[node] = d
			d += 1
			node = edges[node]
			if node == node1 or d1[node] > -1:
				break

		node = node2
		d = 0
		while node != -1:
			d2[node] = d
			d += 1
			node = edges[node]
			if node == node2 or d2[node] > -1:
				break

		x = -1
		mx = float('inf')
		for i in range(n):
			if d1[i] > -1 and d2[i] > -1:
				mxi = max(d1[i], d2[i])
				if mxi<mx:
					mx = mxi
					x = i

		return x
