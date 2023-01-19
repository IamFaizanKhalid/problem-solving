class Solution:
	def subarraysDivByK(self, nums: List[int], k: int) -> int:
		count = 0
		cSum = 0

		remainderCount = [0 for _ in range(k)]

		# setting remainder=0 count to 1 for empty subarray [],
		# so if the whole array has remainder=0, we can subtract this
		# empty subarray in our formula to add that whole to the count
		remainderCount[0] = 1

		for num in nums:
			# cumulative sum
			cSum += num

			remainder = cSum % k

			# if cSum is negative, remainder will be negative but less than -k,
			# adding k to make it positive, and taking mod in case the
			# remainder was positive, adding k will make it >k
			remainder = (remainder + k) % k

			# remainderCount has count of subarrays which has given remainder
			# if sum(0,x) has remainder r and the sum(0,y) has the same remainder,
			# that means sum(0,y)-sum(0,x)=sum(x+1,y) will have remainder=0
			# because we subtracted the sum which has remainder=r
			count += remainderCount[remainder]

			# adding the current to the count too
			remainderCount[remainder]+=1

		return count


		# csum = list(itertools.accumulate(nums))

		# n = len(nums)

		# def sumBtw(i: int, j: int) -> int:
		#	 return csum[j] - (csum[i-1] if i>0 else 0)

		# count = 0
		# for i in range(n):
		#	 for j in range(i, n):
		#		 if sumBtw(i, j) % k == 0:
		#			 count += 1

		# return count
