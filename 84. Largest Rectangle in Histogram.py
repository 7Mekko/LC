class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        res = 0
        for i in range(n):
            if i < n - 1 and heights[i] <= heights[i+1]:
                continue
            min_ = heights[i]
            for j in range(i,-1,-1):
                min_ = min(min_,heights[j])
                res = max(res,min_*(i-j+1))
        return res