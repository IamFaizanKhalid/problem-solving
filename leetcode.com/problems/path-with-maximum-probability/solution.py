class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        paths = defaultdict(list)

        for i, (a,b) in enumerate(edges):
            paths[a].append((b, succProb[i]))
            paths[b].append((a, succProb[i]))


        prob = [0 for _ in range(n)]
        prob[start] = 1.0

        q = [start]

        while q:
            l = len(q)

            for i in q[:l]:
                for adj, p in paths[i]:
                    nprob = prob[i] * p
                    if nprob > prob[adj]:
                        prob[adj] = nprob
                        q.append(adj)

            q = q[l:]

        return prob[end]
