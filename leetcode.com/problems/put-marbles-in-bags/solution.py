class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        pair_weights = []
        for i in range(n-1):
            pair_weights.append(weights[i] + weights[i+1])

        pair_weights.sort()

        pairs = len(pair_weights)
        
        answer = 0
        for i in range(k-1):
            answer += pair_weights[pairs-i-1] - pair_weights[i]
            
        return answer
