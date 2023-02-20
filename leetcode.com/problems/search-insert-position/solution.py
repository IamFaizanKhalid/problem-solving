class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		i, j = 0, len(nums)-1

		while i<=j:
			h = (i+j)//2

			if target == nums[h]:
				return h
			
			if target > nums[h]:
				i = h+1
			else:
				j = h-1

		return j+1
