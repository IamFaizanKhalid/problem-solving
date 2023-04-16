class Solution:
	def numWays(self, words: List[str], target: str) -> int:
		tn = len(target)
		n = len(words)
		l = len(words[0])

		count = [[0 for _ in range(26)] for _ in range(l)]

		chN = lambda c: ord(c) - 97

		for i in range(l):
			for word in words:
				ch = chN(word[i])
				count[i][ch] += 1

		dp = {}
		def recurse(i,ti):
			if ti>=tn:
				return 1
			if i>=l:
				return 0

			if (i,ti) not in dp:
				c = chN(target[ti])

				total = recurse(i+1, ti)
				if count[i][c] > 0:
					total += count[i][c] * recurse(i+1, ti+1)
				
				dp[(i,ti)] = total

			return dp[(i,ti)]

		modulo = (10**9) +7
		return recurse(0,0) % modulo
