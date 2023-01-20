class Solution:
	def findSubsequences(self, nums: List[int]) -> List[List[int]]:
		n = len(nums)
		if n < 2:
			return []

		dp = {}

		def getIncSequences(i: int) -> List[List[int]]:
			if i in dp:
				return dp[i]
			
			if i>=n:
				return []
			
			# sequences excluding current number
			sequences = getIncSequences(i+1)
			
			# sequences including current number
			sI = []
			for sequence in sequences:
				# prepend only if current number is less than next number in sequence
				if nums[i] <= sequence[0]:
					sI += [[nums[i]]+sequence]

			# all sequences combined
			sequences += sI + [[nums[i]]]
			
			dp[i] = sequences

			return sequences

		# converting to set to make unique
		st = set(tuple(x) for x in getIncSequences(0))

		# filtering single value lists
		return [list(s) for s in st if len(s) > 1]
