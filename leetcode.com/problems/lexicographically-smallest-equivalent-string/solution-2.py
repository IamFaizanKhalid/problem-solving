class Solution:
	def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
		rep = [i for i in range(26)]

		def find(x: int) -> int:
			if rep[x] == x:
				return x

			rep[x] = find(rep[x]) 
			return rep[x]
		
		def union(x: int, y: int) -> None:
			x = find(x)
			y = find(y)

			if x < y:
				rep[y] = x
			elif x > y:
				rep[x] = y


		def toChr(i: int) -> str:
			return chr(i+97)
		def toInt(c: str) -> int:
			return ord(c)-97

	   
		for i in range(len(s1)):
			union(toInt(s1[i]), toInt(s2[i]));

		ans = list(baseStr)
		for i, c in enumerate(ans):
			ans[i] = toChr(find(toInt(c)))

		return ''.join(ans)
