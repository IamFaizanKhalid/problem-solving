class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        if n==0:
            return []

        a = 0
        ans = []

        for i in range(1,n):
            if nums[i]-1 != nums[i-1]:
                b = i-1

                if a == b:
                    ans.append(str(nums[a]))
                else:
                    ans.append(str(nums[a])+'->'+str(nums[b]))
                
                a = i

        
        b = n-1
        
        if a == b:
            ans.append(str(nums[a]))
        else:
            ans.append(str(nums[a])+'->'+str(nums[b]))


        return ans
