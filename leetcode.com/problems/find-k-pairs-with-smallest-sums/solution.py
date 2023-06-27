class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)

        pq = [] # (sum, i1)
        for num in nums2:
            sm = nums1[0]+num
            heapq.heappush(pq, (sm, 0))


        pairs = []
        
        while k > 0 and pq:
            sm, i1 = heapq.heappop(pq)

            num1 = nums1[i1]
            num2 = sm - num1

            pairs.append([num1, num2])

            if i1+1 < len(nums1):
                new_sum = nums1[i1+1] + num2
                heapq.heappush(pq, (new_sum, i1+1))

            k -= 1

        return pairs
