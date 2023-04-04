class Solution:
	def partitionString(self, s: str) -> int:
		n = len(s)

		chN = lambda x: ord(x)-97

		lastIndex = [-1 for _ in range(26)]
		
		count = 1
		
		start = 0
		for i in range(n):
			ch = chN(s[i])

			if lastIndex[ch] >= start:
				start = i
				count += 1

			lastIndex[ch] = i

		return count
