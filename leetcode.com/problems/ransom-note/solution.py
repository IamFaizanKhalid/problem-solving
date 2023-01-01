class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		count = [0] * 26

		for c in ransomNote:
			count[ord(c)-97] += 1
		
		for c in magazine:
			count[ord(c)-97] -= 1
		
		for c in count:
			if c > 0:
				return False
		
		return True
