class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)

        events.sort(key = lambda x: tuple(x))


        @cache
        def recurse(i, k):
            if k == 0 or i>=n:
                return 0

            j=i+1
            while j<n and events[j][0]<=events[i][1]:
                j += 1

            pick = events[i][2] + recurse(j, k-1)
            dont = recurse(i+1, k)

            return max(pick, dont)


        return recurse(0,k)
