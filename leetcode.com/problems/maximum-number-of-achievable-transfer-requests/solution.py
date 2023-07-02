class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)

        def are_valid(req_mask):
            diff = [0 for _ in range(n)]

            for i in range(m):
                if req_mask & 1:
                    f,t = requests[i]
                    diff[f] -= 1
                    diff[t] += 1

                req_mask >>= 1
            
            for d in diff:
                if d!=0:
                    return False

            return True


        mask = 2**m - 1

        mx = 0
        while mask >= 0:
            if are_valid(mask):
                mx = max(mx, bin(mask).count('1'))

            mask -= 1

        return mx
