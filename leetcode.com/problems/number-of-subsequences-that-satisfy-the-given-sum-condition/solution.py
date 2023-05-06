class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        modulo = lambda x: x%(10**9 +7)

        nums.sort()
        
        count = 0
        i, j = 0, n-1

        while i <= j:
            if nums[i] + nums[j] <= target:
                count = modulo(count + 2**(j-i))
                i += 1
            else:
                j -= 1

        return count
       
