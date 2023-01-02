class Solution:
	def detectCapitalUse(self, word: str) -> bool:
		if len(word)<2:
			return True
		
		firstCap = ord(word[0])<97
		secondCap = ord(word[1])<97

		if secondCap and not firstCap:
			return False

		for i in range(2,len(word)):
			if not secondCap and ord(word[i])<97:
				return False
			if secondCap and not ord(word[i])<97:
				return False

		return True

