class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size
            

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.table[self._hash(key)].append(key)
        

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.table[self._hash(key)].remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.table[self._hash(key)]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
