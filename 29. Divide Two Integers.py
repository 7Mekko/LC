class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        zf = 1
        ans = 0
        if dividend < 0:
            zf *= -1
            dividend *= -1
        if divisor < 0:
            zf *= -1
            divisor *= -1
        if divisor == 1:
            dividend *= zf
            if dividend <= -2**31 :
                return -2**31
            elif dividend >= 2**31-1:
                return 2**31-1
            return dividend
        while dividend - divisor >= 0:
            i = 1
            while True:
                tmp = divisor
                tmp **= i
                if tmp > dividend:
                    break
                i += 1
            dividend -= divisor**(i-1)
            ans += divisor**(i-2)
        ans *= zf
        return min(max(-2147483648, ans), 2147483647)