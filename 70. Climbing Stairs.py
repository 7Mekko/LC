class Solution:
    def fac(self, n):
        if n == 0:
            return 1
        else:
            return n * Solution.fac(self,n - 1)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 1
        m = n // 2
        while m > 0:
            sum += Solution.fac(self,n-m)//(Solution.fac(self,m)*Solution.fac(self,n-2*m))
            m -= 1
        return sum

    def __init__(self, n):
        self.n = n

    def getAns(self, n):
        print(Solution.climbStairs(self,n))

def main():
    n = 6
    cs = Solution(n)
    cs.getAns(n)
if __name__ == '__main__':
    main()