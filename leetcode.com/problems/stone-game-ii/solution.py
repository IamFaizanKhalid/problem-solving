class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        ALICE = 0
        BOB = 1

        def alice(i,m):
            res = float('-inf')

            sm = 0
            
            for x in range(1, min(2*m, n-i)+1):
                sm += piles[i+x-1]
                    
                res = max(res, sm + recurse(BOB, i+x, max(m,x)))
                    
            return res
        

        def bob(i,m):
            res = float('inf')

            for x in range(1, min(2*m, n-i)+1):
                res = min(res, recurse(ALICE, i+x, max(m,x)))
                    
            return res
        

        @cache
        def recurse(turn,i,m):
            if i == n:
                return 0

            return alice(i,m) if turn==ALICE else bob(i,m)

        return recurse(0,0,1)
        
