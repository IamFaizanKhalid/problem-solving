class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        modulo = lambda x: x % (10**9 + 7)
        
        def recurse(nums):
            if len(nums) < 3: 
                return 1

            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [a for a in nums if a > nums[0]]

            return modulo(
                recurse(left_nodes) * 
                recurse(right_nodes) * 
                math.comb(len(nums)-1, len(left_nodes))
                )
        
        return modulo(recurse(nums)-1)
