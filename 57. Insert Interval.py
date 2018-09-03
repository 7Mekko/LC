# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals = sorted(intervals,key=lambda x:x.start)
        cur = 0
        ans = []
        ans.append(intervals[0])
        n = len(intervals)
        for i in range(1,n):
            if intervals[i].start > ans[cur].end:
                ans.append(intervals[i])
                cur += 1
            else:
                ans[cur].end = max(intervals[i].end,ans[cur].end)
        return ans