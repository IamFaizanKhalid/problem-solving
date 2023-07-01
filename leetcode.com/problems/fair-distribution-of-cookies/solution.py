class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)

        MAX = float('inf')


        given = [0 for _ in range(k)]

        def recurse(i, zeros):
            if n-i < zeros:
                return MAX

            if i>=n:
                return max(given)
            
            mn = MAX
            for kid in range(k):

                z = zeros if given[kid] > 0 else zeros-1
                
                given[kid] += cookies[i]

                mn = min(mn, recurse(i+1, z))

                given[kid] -= cookies[i]

            return mn

        return recurse(0, k)
                
