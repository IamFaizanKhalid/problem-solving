class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # using Kadane's Algorithm to find maximum subarray
        # and mimimum too..
        # mimimum subarray's sum can be subtracted from the total sum
        # to get the sum of other elements to this subarray

        totalSum = 0

        mx = float('-inf')
        totalMax = 0
        
        mn = float('inf')
        totalMin = 0

        # for array upto i
        for num in nums:
            totalSum += num

            # we will choose largest sum between the
            # last max array + i and an array containing only i
            totalMax = max(num, totalMax + num)
            # overall maximum sum will can be this one
            mx = max(mx, totalMax)

            # we will choose smallest sum between the
            # last min array + i and an array containing only i
            totalMin = min(num, totalMin + num)
            # overall minimum sum will can be this one
            mn = min(mn, totalMin)

        # if maximum sum is negative, totalSum will also be negative,
        # because it can't be more than the maximum
        # in this case, we will return the maximum
        # otherwise, we will choose between the maximum of
        # the array in a sequence, and maximum in the circular form
        return mx if mx < 0 else max(mx, totalSum - mn)
