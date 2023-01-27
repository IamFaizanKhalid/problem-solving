class Solution:
	def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
		def chNum(ch):
			return ord(ch)-ord('a')
		
		class TrieNode:
			def __init__(self):
				self.children = [None]*26
				self.endOfWord = False
		
		root = TrieNode()

		def insertIntoTrie(s):
			node = root
		
			for i, ch in enumerate(s):
				c = chNum(ch)
				if not node.children[c]:
					node.children[c] = TrieNode()
				node = node.children[c]

			node.endOfWord = True
		
					
		def isConcated(s, recursive):
			node = root

			for i in range(len(s)):
				c = chNum(s[i])
				if node.endOfWord and isConcated(s[i:], True):
					return True
				if not node.children[c]:
					return False
				node = node.children[c]

			return recursive if node.endOfWord else False

		for word in words:
			insertIntoTrie(word)

		concated = []
		for word in words:
			if isConcated(word, False):
				concated.append(word)

		return concated
