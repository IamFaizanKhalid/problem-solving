class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        k2 = 2*k + 1

        if n < k2:
            return [-1 for _ in range(n)]

        
        avgs = [-1 for _ in range(k)]

        sm = sum(nums[:k2])
        avgs.append(sm//k2)

        for i in range(k2,n):
            sm -= nums[i-k2]
            sm += nums[i]

            avgs.append(sm//k2)


        return avgs +  [-1 for _ in range(k)]
        
