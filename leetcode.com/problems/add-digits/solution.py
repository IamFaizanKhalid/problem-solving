class Solution:
	def addDigits(self, num: int) -> int:
		if num<=9:
			return num
		
		sm = 0
		while num:
			sm+=num%10
			num//=10

		return self.addDigits(sm)
		
