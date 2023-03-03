class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		nc = len(needle)
		hc = len(haystack)

		if hc < nc:
			return -1
			
		ncount = [0 for _ in range(26)]
		hcount = [0 for _ in range(26)]

		chN = lambda ch:ord(ch)-97

		for ch in needle:
			ncount[chN(ch)] += 1
		for ch in haystack[:nc]:
			hcount[chN(ch)] += 1

		match = 0
		for i in range(26):
			if ncount[i] == hcount[i]:
				match += 1

		if match == 26 and haystack[:nc]==needle:
				return 0

		for i in range(nc, hc):
			chAdd = chN(haystack[i])
			hcount[chAdd] += 1
			if hcount[chAdd] == ncount[chAdd]:
				match += 1
			elif  hcount[chAdd] == ncount[chAdd]+1:
				match -= 1

			ri = i-nc
			chRem = chN(haystack[ri])
			hcount[chRem] -= 1
			if hcount[chRem] == ncount[chRem]:
				match += 1
			elif  hcount[chRem] == ncount[chRem]-1:
				match -= 1

			if match == 26 and haystack[ri+1:i+1]==needle:
				return ri+1


		return -1
