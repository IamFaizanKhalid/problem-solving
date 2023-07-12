class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        cycle = [False for _ in range(n)]

        visited = [False for _ in range(n)]

        @cache
        def check(i):
            if visited[i]:
                cycle[i] = True
                return True
            
            visited[i] = True

            for adj in graph[i]:
                if check(adj):
                    cycle[i] = True

            visited[i] = False

            return cycle[i]


        for i in range(n):
            cycle[i] = check(i)

        return [i for i in range(n) if not cycle[i]]
