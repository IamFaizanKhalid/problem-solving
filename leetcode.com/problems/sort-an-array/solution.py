class Solution:
	def sortArray(self, nums: List[int]) -> List[int]:
		heapq.heapify(nums)
		n = len(nums)
		return [heapq.heappop(nums) for _ in range(n)]
