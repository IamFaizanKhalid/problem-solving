class Solution:
	def longestPalindromeSubseq(self, s: str) -> int:
		n = len(s)

		dp = {}

		def longest(l, r):
			if l > r:
				return 0

			if l == r:
				return 1

			if (l,r) not in dp:
				if s[l]==s[r]:
					dp[(l,r)] = longest(l+1, r-1)+2
				else:
					dp[(l,r)] = max(longest(l, r-1), longest(l+1, r))

			return dp[(l, r)]

		return longest(0, n-1)
