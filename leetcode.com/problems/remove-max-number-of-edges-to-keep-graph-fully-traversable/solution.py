class UnionFind:
	def __init__(self, n: int):
		self.group = [i for i in range(n)]
   
	def find(self, x: int) -> int:
		if self.group[x] != x:
			self.group[x] = self.find(self.group[x]) 

		return self.group[x]

	def union(self, x: int, y: int) -> None:
		x = self.find(x)
		y = self.find(y)

		if x < y:
			self.group[y] = x
		elif x > y:
			self.group[x] = y

	def are_connected(self, x: int, y: int) -> bool:
		return self.find(x) == self.find(y)
	 
	def one_group(self) -> bool:
		v = self.find(0)
		for g in self.group:
			if self.find(g) != v:
				return False
		return True
	 

class Solution:
	def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
		uf_alice = UnionFind(n)
		uf_bob = UnionFind(n)

		extra = 0
		for typ,u,v in edges:
			u -= 1
			v -= 1

			if typ == 3:
				if uf_alice.are_connected(u,v) or uf_bob.are_connected(u,v):
					extra += 1
				else:
					uf_alice.union(u,v)
					uf_bob.union(u,v)


		for typ,u,v in edges:
			u -= 1
			v -= 1

			if typ == 1:
				if uf_alice.are_connected(u,v):
					extra += 1
				else:
					uf_alice.union(u,v)

			if typ == 2:
				if uf_bob.are_connected(u,v):
					extra += 1
				else:
					uf_bob.union(u,v)


		return extra if uf_alice.one_group() and uf_bob.one_group() else -1
