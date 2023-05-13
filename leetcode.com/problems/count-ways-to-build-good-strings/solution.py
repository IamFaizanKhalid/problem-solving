class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        modulo = lambda x: x%(1000000007)

        @cache
        def recurse(l=0):
            if l>high:
                return 0
            
            return modulo((l>=low) + recurse(l+zero) + recurse(l+one))


        return recurse()
