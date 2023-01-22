class Solution:
	def partition(self, s: str) -> List[List[str]]:
		isPalindrome = lambda s: s == s[::-1]
		
		n = len(s)
		dp = {}
		
		def recurse(i: int, x: int) -> List[List[str]]:
			if (i,x) in dp:
				return dp[(i,x)]

			cs = s[i:i+1+x]
			if i+x == n-1:
				result = []
				if isPalindrome(cs):
					result += [[cs]]
				dp[(i,x)] = result
				return result

			result = []

			if isPalindrome(cs):
				nx = recurse(i+x+1, 0)
				for nxt in nx:
					result += [[cs] + nxt] 

			nx = recurse(i, x+1)
			if len(nx) > 0:
				result += nx 

			dp[(i,x)] = result
			return result

		return recurse(0, 0)
