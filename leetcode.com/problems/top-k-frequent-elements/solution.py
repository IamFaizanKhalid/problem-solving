class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [x for x, _ in collections.Counter(nums).most_common(k)]
        n = len(nums)


        counts = defaultdict(int)
        for num in nums:
            counts[num] +=1
        

        freqs = [[] for _ in range(n+1)]

        for num, count in counts.items():
            freqs[count].append(num) 


        ans = []
        freq = n
        while k:
            l = len(freqs[freq])
            if k > l:
                ans += freqs[freq]
                k -= l
            else:
                ans += freqs[freq][:k]
                k = 0
            freq -= 1

        return ans
