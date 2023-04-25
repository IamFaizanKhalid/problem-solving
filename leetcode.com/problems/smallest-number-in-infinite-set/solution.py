class SmallestInfiniteSet:

	def __init__(self):
		self.p = 1
		self.q = []
		self.added = {}
		

	def popSmallest(self) -> int:
		if self.q:
			x = heapq.heappop(self.q)
			del self.added[x]
			return x
		
		self.p += 1
		return self.p - 1
		

	def addBack(self, num: int) -> None:
		if num<self.p and num not in self.added:
			self.added[num] = True
			heapq.heappush(self.q, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
