class Solution:
	def mincostTickets(self, days: List[int], costs: List[int]) -> int:
		n = len(days)

		totalCosts = defaultdict(list)

		def minCost(i):
			if i == n-1:
				return min(costs)
			
			if i in totalCosts:
				return totalCosts[i]
			
			j = i+1
			
			while j<n and days[j] < days[i]+7:
				j += 1
			j7 = j

			while j<n and days[j] < days[i]+30:
				j += 1
			j30 = j

			cost30 = costs[2]
			if j30<n:
				cost30 += minCost(j30)
			
			cost7 = costs[1]
			if j7<n:
				cost7 += minCost(j7)

			cost1 = costs[0]
			if i+1<n:
				cost1 += minCost(i+1)

			totalCosts[i] = min(cost1,cost7,cost30)
			
			return totalCosts[i]


		return minCost(0)

