class Solution:
    def __init__(self,x):
        self.x = x

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = '0'
        p = []
        y = 10
        if (x == 0):
            return 0
        if (x < 0):
            p.append('-')
            x = -x
        while(x!=0):
            p.append(x%y)
            x //= y
        ans = ''.join('%s' %id for id in p)
        int_ = int(ans)
        if ((int_ > 2 ** 31 - 1) or (int_ < -2 ** 31)):
            return 0
        return int_

    def getans(self,x):
        print(Solution.reverse(self,x))


def main():
    x = -120432
    a = Solution(x)
    a.getans(x)


if __name__ == '__main__':
    main()