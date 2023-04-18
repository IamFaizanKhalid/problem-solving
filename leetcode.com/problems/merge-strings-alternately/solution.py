class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
		m = len(word1)
		n = len(word2)
		x = min(m,n)

		result = ""
		for i in range(x):
			result += word1[i] + word2[i]

		for i in range(x,m):
			result += word1[i]

		for i in range(x,n):
			result += word2[i]

		return result
