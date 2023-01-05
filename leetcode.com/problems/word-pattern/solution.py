class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		arr = s.split()

		if len(arr) != len(pattern):
			return False

		x = {}
		y = {}
		for i, word in enumerate(arr):
			c = pattern[i]

			if c in x and x[c]!=word:
				return False

			if word in y and y[word]!=c:
				return False
			
			x[c]=word
			y[word]=c

		return True
