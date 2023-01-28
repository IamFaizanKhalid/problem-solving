class SummaryRanges:
	def __init__(self):
		self.nums = set()
		
	def addNum(self, value: int) -> None:
		self.nums.add(value)

	def getIntervals(self) -> List[List[int]]:
		intervals = []
		done = set()
		for num in self.nums:
			if num in done: 
				continue

			left = num
			while left - 1 in self.nums:
				left -= 1
				done.add(left)

			right = num
			while right + 1 in self.nums:
				right += 1
				done.add(right)

			intervals.append([left, right])

		return sorted(intervals)

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
