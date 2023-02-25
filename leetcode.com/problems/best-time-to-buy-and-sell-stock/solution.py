class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		# m = 0
		# for x, i in enumerate(prices):
		#	 for j in prices[x+1:]:
		#		 m = max(m, j-i)

		# return m

		profit = 0
		smallest = prices[0]
		for price in prices[1:]:
			if price < smallest:
				# if the price is smallest, the maximum profit after this day will be with this price
				smallest = price
			else:
				# calculating profit with smallest price appear before
				profit = max(profit, price-smallest)

		return profit
