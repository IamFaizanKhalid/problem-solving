class Solution:
	def isScramble(self, s1: str, s2: str) -> bool:
		if len(s1) != len(s2):
			return False

		dp = {}

		def match(s1, s2):
			if (s1,s2) not in dp:
				if s1==s2:
					dp[(s1,s2)] = True
				else:
					dp[(s1,s2)] = False

					for i in range(1, len(s1)): # it skips n=1
						if (
							( match(s1[:i],s2[:i]) and match(s1[i:],s2[i:]) )
								or
							( match(s1[:i],s2[-i:]) and match(s1[i:],s2[:-i]) )
						):
							dp[(s1,s2)] = True
							break

			return dp[(s1,s2)]

		return match(s1,s2)
			
			
