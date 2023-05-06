class Solution:
	def maxVowels(self, s: str, k: int) -> int:
		n = len(s)
		isVowel = lambda x: "aeiou".find(x) > -1

		c = 0
		for i in range(min(n,k)):
			if isVowel(s[i]):
				c += 1

		mc = c

		for i in range(k,n):
			if isVowel(s[i-k]):
				c -= 1
			
			if isVowel(s[i]):
				c += 1
			
			mc = max(mc,c)

		return mc
