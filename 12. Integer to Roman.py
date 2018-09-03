class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m4 = num // 1000
        num %= 1000
        m3 = num // 100
        num %= 100
        m2 = num // 10
        num %= 10
        m1 = num // 1
        str = ''
        while m4:
            str += 'M'
            m4 -= 1
        if m3 == 4 :
            str += 'CD'
        elif m3 == 9 :
            str += 'CM'
        else:
            if m3 // 5 :
                str += 'D'
                m3 -= 5
            while m3:
                str += 'C'
                m3 -= 1
        if m2 == 4 :
            str += 'XL'
        elif m2 == 9 :
            str += 'XC'
        else:
            if m2 // 5 :
                str += 'L'
                m2 -= 5
            while m2:
                str += 'X'
                m2 -= 1
        if m1 == 4 :
            str += 'IV'
        elif m1 == 9 :
            str += 'IX'
        else:
            if m1 // 5 :
                str += 'V'
                m1 -= 5
            while m1:
                str += 'I'
                m1 -= 1
        return str

    def getans(self, num):
        print(Solution.intToRoman(self, num))

    def __init__(self, num):
        self.num = num

def main():
    int_ = 1994
    a = Solution(int_)
    a.getans(int_)

if __name__ == '__main__':
    main()