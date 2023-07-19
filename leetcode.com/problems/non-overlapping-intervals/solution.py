class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        intervals.sort(key=lambda x: x[1])

        total = 0

        last_end = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start < last_end:
                total += 1
            else:
                last_end = end
        
        return total
