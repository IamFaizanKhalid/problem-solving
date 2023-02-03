class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1:
			return s

		lines = ["" for _ in range(numRows)]

		upwards = False
		l = 0
		for c in s:
			lines[l] += c

			l = l-1 if upwards else l+1
			
			if l == 0 or l == numRows-1:
				upwards = not upwards

		return ''.join(lines)
