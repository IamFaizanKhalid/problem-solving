class Solution:
	def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
		alts = defaultdict(list)

		for i in range(len(s1)):
			alts[s1[i]].append(s2[i])
			alts[s2[i]].append(s1[i])

		rep = [chr(97+i) for i in range(26)]
		visited = [False for i in range(26)]  

		def update(ch, rp):
			i = ord(ch)-97
			if visited[i]:
				return

			visited[i] = True
			for x in alts[ch]:
				update(x, rp)
			visited[i] = False

			rep[i] = rp
			del alts[ch]

		for i in range(26):
			c = chr(i+97)
			update(c, min(c, rep[i]))

		l = list(baseStr)
		for i, c in enumerate(l):
			l[i] = rep[ord(c)-97]

		return ''.join(l)
