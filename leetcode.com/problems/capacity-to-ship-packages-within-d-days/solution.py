class Solution:

	def shipWithinDays(self, weights: List[int], days: int) -> int:



		def daysNeeded(shipCapacity):

			d = 1

			load = 0



			for w in weights:

				load += w

				if load > shipCapacity:

					d+=1

					load = w



			return d





		minCapacity = max(weights) # ship should be able to hold max weight pkg

		maxCapacity = sum(weights) # should don't need to be more than the total weight



		while minCapacity < maxCapacity:

			# binary approach

			capacity = (minCapacity+maxCapacity)//2



			if daysNeeded(capacity) <= days:

				# if all pkgs can be shipped within given days with this capacity, min capacity can't be more

				maxCapacity = capacity

			else:

				# if all pkgs can't be shipped within given days with this capacity, min capacity will be more

				minCapacity = capacity + 1

			

		return minCapacity

