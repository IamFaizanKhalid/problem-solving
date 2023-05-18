class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        incoming = [False for _ in range(n)]   
        
        for _,to in edges:
            incoming[to] = True

        result = []
        for i in range(n):
            if not incoming[i]:
                result.append(i)

        return result
        # return [i for i, x in enumerate(incoming) if not x]
