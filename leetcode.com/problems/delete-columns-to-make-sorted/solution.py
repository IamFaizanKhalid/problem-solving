class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l = len(strs[0])

        toRemoveCount = 0

        for c in range(l):
            sorted=True
            x = strs[0][c]
            for i in range(len(strs)):
                if strs[i][c]<x:
                    return False
                x = strs[i][c]
            if not sorted:
                toRemoveCount+=1

        return toRemoveCount

    

            
