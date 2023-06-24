class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)

        @cache
        def recurse(i, diff):
            if i>=n:
                return 0 if diff==0 else float('-inf')

            l = rods[i]

            skip = recurse(i+1, diff) # diff will remain the same

            add_to_long = recurse(i+1, diff+l) # diff will increase
            
            add_to_short = recurse(i+1, abs(diff-l)) # diff will decrease
            add_to_short += min(diff, l) # adding previously equal lenghts
            
            return max(skip, add_to_long, add_to_short)
            
        return recurse(0,0)
