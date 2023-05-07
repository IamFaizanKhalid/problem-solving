class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)

        ans = [1 for _ in range(n)]

        sequence = []
        for i in range(n):
            si = bisect.bisect_right(sequence, obstacles[i])
            
            if si == len(sequence):
                sequence.append(obstacles[i])
            else:
                sequence[si] = obstacles[i]

            ans[i] = si+1
          

        return ans
