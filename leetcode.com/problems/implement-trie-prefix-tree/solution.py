class TrieNode:
	def __init__(self, val):
		self.val = val
		self.isLeaf = False
		self.childs = [None]*26


class Trie:

	def __init__(self):
		self.root = TrieNode(None)
		

	def insert(self, word: str) -> None:
		cN = lambda c: ord(c)-97

		root = self.root

		for ch in word:
			i = cN(ch)
			if not root.childs[i]:
				root.childs[i] = TrieNode(ch)
				
			root = root.childs[i]

		root.isLeaf = True
		

	def search(self, word: str) -> bool:
		cN = lambda c: ord(c)-97

		root = self.root

		for ch in word:
			i = cN(ch)
			if not root.childs[i]:
				return False
				
			root = root.childs[i]

		return root.isLeaf
		

	def startsWith(self, prefix: str) -> bool:
		cN = lambda c: ord(c)-97

		root = self.root

		for ch in prefix:
			i = cN(ch)
			if not root.childs[i]:
				return False
				
			root = root.childs[i]

		return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
