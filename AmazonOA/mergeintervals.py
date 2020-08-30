class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals)<=1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        cur = intervals[0]
        start = cur[0]
        end = cur[1]
        res =[]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=end:
                end = max(end,intervals[i][1])
            else:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start,end])
        return res








