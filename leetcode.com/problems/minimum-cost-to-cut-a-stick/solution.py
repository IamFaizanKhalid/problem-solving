class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        
        @cache
        def recurse(start, end):
            if end-start == 1:
                return 0
                
            mn = float('inf')
            for cut in range(start+1, end):
                cost = recurse(start, cut) + recurse(cut, end)
                mn = min(mn, cost)

            return mn + (cuts[end] - cuts[start])
        
        return recurse(0, len(cuts)-1)
