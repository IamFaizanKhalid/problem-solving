class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        if n <= k:
            return sum(costs)

        remI = candidates
        remJ = n-candidates-1

        pq = []
        if candidates*2 < n:
            for (i, cost) in enumerate(costs[:remI]):
                heapq.heappush(pq, (cost, i))
            for (i, cost) in enumerate(costs[remJ+1:]):
                heapq.heappush(pq, (cost, remJ+1+i))
        else:
            for i, cost in enumerate(costs):
                heapq.heappush(pq, (cost, i))

        total = 0

        while k>0:
            cost, i = heapq.heappop(pq)
            total += cost
            k -= 1

            if remI <= remJ:
                if i<remI:
                    heapq.heappush(pq, (costs[remI], remI))
                    remI += 1
                else:
                    heapq.heappush(pq, (costs[remJ], remJ))
                    remJ -= 1


        return total
 
