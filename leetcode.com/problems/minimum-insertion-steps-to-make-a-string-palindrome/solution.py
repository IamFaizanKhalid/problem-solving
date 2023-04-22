class Solution:
	def minInsertions(self, s: str) -> int:

		@cache
		def recurse(i,j):
			if i>=j:
				return 0

			if s[i] == s[j]:
				return recurse(i+1,j-1)
			else:
				return 1+min(recurse(i+1,j),recurse(i,j-1))

		return recurse(0,len(s)-1)
