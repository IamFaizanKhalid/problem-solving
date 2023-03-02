class Solution:
	def compress(self, chars: List[str]) -> int:
		n = len(chars)
		i, j = 0, 0

		while j < n:
			chars[i]=chars[j]
			same = 1

			k = j+1
			while k < n:
				if chars[j] != chars[k]:
					j = k-1
					break
				same += 1
				k += 1

			if k == n:
				j = n
			
			j += 1
			i += 1
			
			if same>1:
				for ch in str(same):
					chars[i] = ch
					i += 1
			
		return i
