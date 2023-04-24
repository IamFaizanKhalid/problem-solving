class Solution:
	def lastStoneWeight(self, stones: List[int]) -> int:
		stones = [-w for w in stones]
		heapq.heapify(stones)

		while len(stones)>1:
			st1=-heapq.heappop(stones)
			st2=-heapq.heappop(stones)

			diff = st1-st2
			if diff > 0:
				heapq.heappush(stones,-diff)

		return 0 if len(stones)==0 else -stones[0]
