class Solution:
	def minimizeArrayValue(self, nums: List[int]) -> int:
		mn = 0

		sm = 0
		for i,num in enumerate(nums):
			sm += nums[i]
			average = math.ceil(sm/(i+1))

			mn = max(mn, average)

		return mn
