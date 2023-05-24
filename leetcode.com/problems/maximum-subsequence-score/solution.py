class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)

        sortedIndex = [i for i,_ in sorted(enumerate(nums2), key=lambda x:x[1], reverse=True)]

        nums1 = [nums1[i] for i in sortedIndex]
        nums2 = [nums2[i] for i in sortedIndex]


        pq = nums1[:k]
        heapq.heapify(pq)

        sm = sum(pq)
        
        mx = sm*nums2[k-1] # minimum in nums2 subsequence
        
        for i in range(k, n):
            # remove minimum from nums2 and add next (largest if remaining)

            heapq.heappush(pq, nums1[i])
            sm += nums1[i]
            sm -= heapq.heappop(pq)
            
            mx = max(mx, sm*nums2[i])
        
        
        return mx
