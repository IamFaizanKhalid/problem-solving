class Solution:
	def findKthPositive(self, arr: List[int], k: int) -> int:
		n = len(arr)

		i, j = 0, n-1

		while i<=j:
			h = (i+j)//2

			diff = arr[h] - (h+1)

			if diff < k:
				i = h + 1
			else:
				j = h - 1

		return i + k
