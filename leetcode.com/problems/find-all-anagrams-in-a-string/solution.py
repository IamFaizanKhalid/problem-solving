class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		ls, lp = len(s), len(p)

		if ls < lp:
			return []

		cN = lambda x: ord(x)-97

		cP = [0 for _ in range(26)]
		for c in p:
			cP[cN(c)] += 1

		cS = [0 for _ in range(26)]
		for c in s[:lp]:
			cS[cN(c)] += 1

		sameFreqCount = 0
		for i in range(26):
			if cS[i] == cP[i]:
				sameFreqCount += 1

		result = []
		if sameFreqCount == 26:
			result.append(0)

		for i in range(0, ls-lp):
			chRem = cN(s[i])
			cS[chRem] -= 1
			if cS[chRem] == cP[chRem]:
				sameFreqCount += 1
			elif cS[chRem] == cP[chRem] - 1:
				sameFreqCount -= 1

			chAdd = cN(s[i+lp])
			cS[chAdd] += 1
			if cS[chAdd] == cP[chAdd]:
				sameFreqCount += 1
			elif cS[chAdd] == cP[chAdd] + 1:
				sameFreqCount -= 1

			if sameFreqCount == 26:
				result.append(i+1)

		return result
