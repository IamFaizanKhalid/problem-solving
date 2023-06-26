class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        modulo = lambda x: x%1000000007

        @cache
        def recurse(i, fuel):
            total = 1 if i==finish else 0

            if fuel == 0:
                return total

            for j in range(n):
                req = abs(locations[j]-locations[i])
                if 0 < req <= fuel: # distinct
                    total = modulo(total + recurse(j, fuel-req))


            return total


        return recurse(start,fuel)
