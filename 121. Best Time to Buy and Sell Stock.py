class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l <= 1:
            return 0
        max_ = 0
        min_ = prices[0]
        for i in range(l):
            max_ = max(max_, prices[i] - min_);
            min_ = min(min_, prices[i]);
        return max_
