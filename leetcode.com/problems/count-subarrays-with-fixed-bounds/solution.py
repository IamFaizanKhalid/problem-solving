class Solution:
	def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
		start, mi,mj = -1,-1,-1

		count = 0

		for i in range(len(nums)):
			x = nums[i]

			if minK <= x and x <= maxK:
				
				if x == minK:
					mi = i
				
				if x == maxK:
					mj = i
					
			else:
				start = i

			count += max(0, min(mi, mj) - start)
			
		return count
