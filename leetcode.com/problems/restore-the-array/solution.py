class Solution:
	def numberOfArrays(self, s: str, k: int) -> int:
		n = len(s)
		modulo = (10**9) + 7

		digit = lambda x: ord(x)-48

		@cache
		def recurse(i):
			if i>=n:
				return 1
			
			if s[i] == '0':
				return 0

			total = 0
			d = 0
			for j in range(i, n):
				d = d*10 + digit(s[j])
				if d > k:
					break

				total = (total + recurse(j+1)) % modulo

			return total

		
		return recurse(0)
