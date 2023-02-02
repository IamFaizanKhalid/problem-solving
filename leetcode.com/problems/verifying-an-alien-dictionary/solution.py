class Solution:
	def isAlienSorted(self, words: List[str], order: str) -> bool:
		chNum = lambda c: ord(c)-97

		chIndex = [0 for _ in range(26)]

		for i, c in enumerate(order):
			chIndex[chNum(c)] = i

		def isSmaller(word, than):
			lw = len(word)
			lt = len(than)

			lm = min(lw, lt)

			for i in range(lm):
				if chIndex[chNum(word[i])] != chIndex[chNum(than[i])]:
					return chIndex[chNum(word[i])] < chIndex[chNum(than[i])]

			return lw < lt


		for i in range(1, len(words)):
			if isSmaller(words[i], words[i-1]):
				return False
		
		return True
