class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        paths = defaultdict(list)

        for i in range(len(equations)):
            a,b = equations[i]
            paths[a].append((b, values[i]))
            paths[b].append((a, 1/values[i]))


        def bfs(startVar, targetVar):
            if startVar not in paths or targetVar not in paths:
                return -1.0

            visited = defaultdict(bool)

            q = [(startVar, 1.0)]
            while q:
                n = len(q)

                for i in range(n):
                    var, cost = q[i]
                    
                    if var == targetVar:
                        return cost
                    
                    visited[var] = True
                    
                    for adjVar, adjCost in paths[var]:
                        if not visited[adjVar]:
                            q.append((adjVar, cost*adjCost))

                q = q[n:]

            return -1.0


        return [bfs(c,d) for c,d in queries]
