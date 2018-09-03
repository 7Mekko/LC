class Solution:
    def __init__(self, s, numRows):
        self.s = s
        self.numRows = numRows

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s
        l = 2 * numRows - 2
        p = []

        for i in range(numRows):
            p.append('')
        for i in range(len(s)):
            if (i % l <= numRows - 1):
                p[i%l] += s[i]
            else:
                p[(l-i)%l] += s[i]
        str_ = ''
        for i in range(numRows):
            str_ += p[i]
        return str_


    def getans(self,s,numRows):
        print(Solution.convert(self,s,numRows))


def main():
    s = "A"
    numRows = 1
    a = Solution(s,numRows)
    a.getans(s,numRows)


if __name__ == '__main__':
    main()
