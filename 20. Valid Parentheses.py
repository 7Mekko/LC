class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = '0'
        cnt = 0
        if len(s)%2 == 1:
            return False
        for str_ in s:
            if str_ == '(' or str_ == '[' or str_ == '{':
                tmp += str_
                cnt += 1
            if str_ == ')':
                if tmp[cnt] == '(':
                    tmp = tmp[0:cnt]
                    cnt -= 1
                else:
                    return False
            if str_ == '}':
                if tmp[cnt] == '{':
                    tmp = tmp[0:cnt]
                    cnt -= 1
                else:
                    return False
            if str_ == ']':
                if tmp[cnt] == '[':
                    tmp = tmp[0:cnt]
                    cnt -= 1
                else:
                    return False
        if tmp == '0':
            return True
        return False

    def __init__(self, s):
        self.s = s

    def getAns(self, s):
        print(Solution.isValid(self, s))

def main():
    s = "()("
    iv = Solution(s)
    iv.getAns(s)

if __name__ == '__main__':
    main()