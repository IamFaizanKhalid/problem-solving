class Solution:
	def singleNonDuplicate(self, nums: List[int]) -> int:
		i, j = 0, len(nums)-1

		while i <= j:
			h = (i+j)//2

			even = h%2==0

			if h-1>=0 and nums[h-1] == nums[h]:
				if even:
					j = h-2
				else:
					i = h+1
			elif h+1<len(nums) and nums[h+1] == nums[h]:
				if even:
					i = h+2
				else:
					j = h-1
			else:
				return nums[h]
