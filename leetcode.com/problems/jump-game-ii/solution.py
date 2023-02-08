class Solution:
	def jump(self, nums: List[int]) -> int:
		n = len(nums)

		minJumps = [-1 for _ in range(n)]

		def jumpRecursive(i):
			if i >= n:
				return float('inf')
			if i == n-1:
				return 0

			if minJumps[i] > -1:
				return minJumps[i]
 
			js = nums[i]

			minJ = float('inf')
			for j in range(1,js+1):
				minJ = min(minJ, jumpRecursive(i+j))

			if minJ < float('inf'):
				minJ += 1

			minJumps[i] = minJ

			return minJ

		return jumpRecursive(0)
