class Solution:
	def gcdOfStrings(self, str1: str, str2: str) -> str:
		l1, l2 = len(str1), len(str2)
		
		# the result string cannot be longer than the smaller string
		minLen = min(l1, l2)

		for l in range(minLen, 0, -1):
			# if both string can be splitted in strings of length l
			if l1 % l == 0 and l2 % l == 0:
				
				# the length l string
				s = str1[:l]

				# number of times the string will repeat
				rep1 = l1 // l
				rep2 = l2 // l

				# if repeating the string s make the actual strings,
				# it is the answer
				if str1 == s*rep1 and str2 == s*rep2:
					return s

		return ""
