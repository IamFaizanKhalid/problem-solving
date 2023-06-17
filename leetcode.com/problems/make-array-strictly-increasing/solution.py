class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        INT_MAX = float('INF')

        n = len(arr1)
        n2 = len(arr2)


        def get_next_smallest(num):
            l, r = 0, n2

            while l<r:
                m = (l+r)//2

                if arr2[m] <= num:
                    l = m + 1
                else:
                    r = m

            return -1 if l>=n2 else arr2[l]


        @cache
        def check(i, p):
            if i == n:
                return 0

            c = arr1[i]

            mn = INT_MAX

            if p < c:
                mn = min(mn, check(i+1, c))

            c = get_next_smallest(p)

            if c != -1:
                mn = min(mn, check(i+1, c)+1)

            return mn            
                
        
        ans = check(0, -1)
        
        return -1 if ans==INT_MAX else ans
            
