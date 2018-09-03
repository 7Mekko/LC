class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 1
        r = (x + 1) // 2
        while l < r:
            m = (l + r) // 2
            s = m * m
            if s == x:
                return m
            if s < x:
                l = m + 1
            else:
                r = m - 1
        s = r * r
        if s > x:
            return r - 1
        return r