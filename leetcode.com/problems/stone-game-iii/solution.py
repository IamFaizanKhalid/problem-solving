class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)
        ALICE = 0
        BOB = 1

        @cache
        def recurse(turn, i):
            if i == n:
                return 0,0

            if turn == ALICE:
                a,b = recurse(BOB, i+1)
                mxa = stoneValue[i] + a
                mxb = b

                if i+1<n:
                    a,b = recurse(BOB, i+2)
                    a += stoneValue[i] + stoneValue[i+1]

                    if a>mxa:
                        mxa = a
                        mxb = b
                    
                if i+2<n:
                    a,b = recurse(BOB, i+3)
                    a += stoneValue[i] + stoneValue[i+1] + stoneValue[i+2]

                    if a>mxa:
                        mxa = a
                        mxb = b

                return mxa, mxb

            else:
                a,b = recurse(ALICE, i+1)
                mxa = a
                mxb = stoneValue[i] + b

                if i+1<n:
                    a,b = recurse(ALICE, i+2)
                    b += stoneValue[i] + stoneValue[i+1]

                    if b>mxb:
                        mxa = a
                        mxb = b
                    
                if i+2<n:
                    a,b = recurse(ALICE, i+3)
                    b += stoneValue[i] + stoneValue[i+1] + stoneValue[i+2]

                    if b>mxb:
                        mxa = a
                        mxb = b

                return mxa, mxb


        a,b = recurse(ALICE,0)

        if a==b:
            return "Tie"

        return "Alice" if a>b else "Bob"
