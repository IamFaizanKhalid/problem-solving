class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)

        chN = lambda c: ord(c)-97
        nCh = lambda n: chr(n+97)

        counts = [0 for _ in range(26)]
        for ch in s:
            counts[chN(ch)] += 1


        def variance(i,j):
            A = nCh(i)
            B = nCh(j)
            nA = 0
            nB = 0
            nB_remaining = counts[j]

            
            mx_diff = 0

            for ch in s:
                if ch == A:
                    nA += 1
                if ch == B:
                    nB += 1
                    nB_remaining -= 1

                if nB > 0:
                    mx_diff = max(mx_diff, nA-nB)

                if nA < nB and nB_remaining > 0:
                    nA = 0
                    nB = 0

            return mx_diff


        ans = 0

        for i in range(26):
            for j in range(26):
                if i != j and counts[i] and counts[j]:
                    ans = max(ans, variance(i,j))
               
        return ans
