class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0) or ((x % 10 == 0) and (x != 0)):
            return False
        length = 0
        y = x
        while y:
            y //= 10
            length += 1
        for i in range(1,length//2+1):
            if (x // (10 ** (length - 2 * i + 1))) == (x % 10):
                x = (x % (10 ** (length - 2 * i +1))) // 10
                continue
            else:
                return False
        return True


    def __init__(self, x):
        self.x = x
    def getans(self, x):
        print(Solution.isPalindrome(self,x)
)
def main():
    x = 1568651
    a = Solution(x)
    a.getans(x)


if __name__ == '__main__':
    main()