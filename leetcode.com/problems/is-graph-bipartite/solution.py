class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        group = [-1 for _ in range(n)]

        def bipartite(x):
            q = [x]
            g = 0

            while q:
                c = len(q)

                for i in range(c):
                    node = q[i]

                    group[node] = g

                    for adj in graph[node]:
                        match group[adj]:
                            case 0:
                                if g == 0:
                                    return False
                            case 1:
                                if g == 1:
                                    return False
                            case default:
                                q.append(adj)


                g = (g+1)%2
                q = q[c:]

            return True

        for i in range(n):
            if group[i]==-1:
                if not bipartite(i):
                    return False

        return True
