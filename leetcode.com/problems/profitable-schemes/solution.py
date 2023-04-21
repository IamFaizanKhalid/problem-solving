class Solution:
	def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
		l = len(group)

		@cache
		def recurse(i, n, curProfit):
			if i>=l or n==0:
				if curProfit>=minProfit:
					return 1
				return 0

			total = 0

			if group[i] <= n:
				total += recurse(i+1,n-group[i],min(minProfit,curProfit+profit[i]))

			total += recurse(i+1, n, curProfit)

			return total


		modulo = 10**9 + 7
		
		return recurse(0,n,0)%modulo
