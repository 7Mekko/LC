class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        m = len(t)
        i = l = r = 0
        dic = collections.Counter(t)
        for j,c in enumerate(s,1):
            m -= dic[c] > 0
            dic[c] -= 1
            if not m:
                while i < j and dic[s[i]] < 0:
                    dic[s[i]] += 1
                    i += 1
                if not r or j - i <= r - l:
                    l , r = i , j
        return s[l:r]
    def __init__(self, s, t):
        self.s = s
        self.t = t
    def getAns(self, s, t):
        print(Solution.minWindow(self,s,t))

def main():
    s = "Ab"
    t = "A"
    S = Solution(s,t)
    S.getAns(s,t)
if __name__ == '__main__':
    main()