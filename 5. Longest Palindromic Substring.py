class Solution:
    def __init__(self,s):
        self.s = s
    '''
    Manacher算法
    '''
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_new = []
        s_new.append('$')
        s_new.append('#')
        for i in range(len(s)):
            s_new.append(s[i])
            s_new.append('#')
        s_new.append(None)
        p = []
        p.append(None)
        for i in range(len(s_new)-1):
            p.append(0)
        mx = 0
        id = 0
        for i in range(1,len(s_new)-1):
            if (i < mx):
                p[i] = min(p[2*id - i] ,mx - i)
            else:
                p[i] = 1
            while(s_new[i-p[i]] == s_new[i+p[i]]):
                p[i] += 1
            if (mx < i + p[i]):
                id = i
                mx = i + p[i]
        max_ = 1
        for i in range(1,len(p)):
            if p[i] > p[max_]:
                max_ = i
        str_ = s_new[max_-p[max_]+1:max_+p[max_]]
        for i in range(len(str_)//2+1):
            str_.remove('#')
        str_ = ''.join(str_)
        return str_


    def getans(self,s):
        print(Solution.longestPalindrome(self,s))


def main():
    s = input()
    a = Solution(s)
    a.getans(s)


if __name__ == '__main__':
    main()