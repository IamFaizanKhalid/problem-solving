class Solution:
	def minimumDeviation(self, nums: List[int]) -> int:
		class MaxHeap:
		# heapq is a min heap, but we need a max heap
		# so we will store negated elements
		
			def __init__(self):
				self.q = []
			def push(self, e):
				heapq.heappush(self.q, -e)
			def pop(self):
				return -heapq.heappop(self.q)
			def top(self):
				return -self.q[0]
		

		evens = MaxHeap()

		mn = float('inf')

		# pushing all numbers converted to evens
		for num in nums:
			if num % 2 == 0:
				evens.push(num)
				mn = min(num, mn)
			else:
				evens.push(num*2)
				mn = min(num*2, mn)				

		# dividing the maximum by 2 and calculating difference
		diff = float('inf')
		while evens.top() % 2 == 0:
			mx = evens.pop()
			diff = min(diff, mx-mn)

			x = mx // 2
			evens.push(x)
			mn = min(x, mn)

		diff = min(diff, evens.top()-mn)

		return diff
