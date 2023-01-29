class LFUCache:

	def __init__(self, capacity: int):
		self.capacity = capacity
		self.minFreq = float('inf') # key with minimum frequency
		self.cache = dict() # key value pair
		self.lastUsedWithFreq = defaultdict(deque) # queue with last used on the left
		self.keysWithFreq = defaultdict(set) # set to keep keys unqiue without need to search

	def get(self, key: int) -> int:
		if key not in self.cache:
			return -1
		
		value, _ = self.cache[key]
		self.update(key, value) # updating the frequency

		return value

	def put(self, key: int, value: int) -> None:
		if self.capacity == 0:
			return

		if key not in self.cache:
			self.add(key, value, 1)
		else:
			self.update(key, value)


	def makeSpace(self):
		if len(self.cache) < self.capacity:
			return
			
		minFreqLastUsed = self.lastUsedWithFreq[self.minFreq].pop()

		self.keysWithFreq[self.minFreq].remove(minFreqLastUsed)
		del self.cache[minFreqLastUsed]


	def add(self, key, value, freq):
		self.makeSpace()
		
		self.minFreq = min(self.minFreq, freq)
		self.lastUsedWithFreq[freq].appendleft(key)
		self.keysWithFreq[freq].add(key)
		self.cache[key] = (value, freq)


	def delete(self, key):
		_, freq = self.cache[key]
		
		self.lastUsedWithFreq[freq].remove(key)
		self.keysWithFreq[freq].remove(key)
		
		if len(self.lastUsedWithFreq[freq]) == 0:
			del self.lastUsedWithFreq[freq]
			
			if freq == self.minFreq:
				self.minFreq += 1

		del self.cache[key]


	def update(self, key, value):
		_, freq = self.cache[key]		
		self.delete(key)
		self.add(key, value, freq+1)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
