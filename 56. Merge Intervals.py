# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n <= 1:
            return intervals
        ans = []
        intervals = sorted(intervals, key=lambda x:x.start)
        cur = 0
        ans.append(intervals[0])
        for i in range(1,n):
            if intervals[i].start > ans[cur].end:
                ans.append(intervals[i])
                cur += 1
            else:
                ans[cur].end = max(intervals[i].end,ans[cur].end)
        return ans