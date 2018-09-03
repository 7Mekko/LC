class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        list_ = []
        for rstr in s:
            if rstr == 'M':
                list_.append(1000)
            if rstr == 'D':
                list_.append(500)
            if rstr == 'C':
                list_.append(100)
            if rstr == 'L':
                list_.append(50)
            if rstr == 'X':
                list_.append(10)
            if rstr == 'V':
                list_.append(5)
            if rstr == 'I':
                list_.append(1)
        list_.append(0)
        for i in range(len(list_)-1):
            if list_[i] < list_[i+1]:
                list_[i] = 0 - list_[i]
        for i in range(len(list_)):
            sum += list_[i]
        return sum

    def getans(self, s):
        print(Solution.romanToInt(self, s))

    def __init__(self, s):
        self.s = s

def main():
    str_ = "MCMXCIV"
    a = Solution(str_)
    a.getans(str_)

if __name__ == '__main__':
    main()