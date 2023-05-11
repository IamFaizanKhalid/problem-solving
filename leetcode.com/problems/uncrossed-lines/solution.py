class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)

        @cache
        def recurse(i,j):
            if i>=l1 or j>=l2:
                return 0

            count = max(recurse(i+1,j), recurse(i,j+1))

            if nums1[i]==nums2[j]:
                count = max(count, 1+recurse(i+1,j+1))

            return count

        return recurse(0,0)
