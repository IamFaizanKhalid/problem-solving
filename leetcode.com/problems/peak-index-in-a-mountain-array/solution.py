class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)

        l = 0
        r = n-1

        while l<r:
            m = (l+r)//2

            if arr[m]<arr[m+1]:
                l = m+1
            else:
                r = m
        
        return l
