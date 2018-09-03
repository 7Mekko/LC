class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        import math
        a = math.factorial(m + n - 2)
        b = math.factorial(m - 1)
        c = math.factorial(n - 1)
        cnt = a // (b * c)
        return cnt



