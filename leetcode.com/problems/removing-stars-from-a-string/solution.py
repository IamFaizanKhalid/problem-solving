class Solution:
	def removeStars(self, s: str) -> str:
		n = len(s)

		ns =""
		stars = 0

		for i in range(n-1,-1,-1):
			if s[i]=="*":
				stars += 1
			else:
				if stars==0:
					ns = s[i]+ns
				else:
					stars -= 1

		return ns
