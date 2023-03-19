class TrieNode:
	def __init__(self, val):
		self.val = val
		self.isLeaf = False
		self.childs = [None]*26
		
	def match(self, word):
		cN = lambda c: ord(c)-97

		if len(word) == 0:
			return self.isLeaf

		if word[0]=='.':
			for i in range(26):
				if self.childs[i] and self.childs[i].match(word[1:]):
					return True
			return False

		i = cN(word[0])
		if not self.childs[i]:
			return False
			
		return self.childs[i].match(word[1:])



class WordDictionary:

  def __init__(self):
		  self.root = TrieNode(None)
	

  def addWord(self, word: str) -> None:
		  cN = lambda c: ord(c)-97

		  root = self.root

		  for ch in word:
			  i = cN(ch)
			  if not root.childs[i]:
				root.childs[i] = TrieNode(ch)

			  root = root.childs[i]

		  root.isLeaf = True
	

  def search(self, word: str) -> bool:
		  return self.root.match(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
