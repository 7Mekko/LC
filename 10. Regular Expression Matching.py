class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p_len = len(p)
        s_len = len(s)
        dp = [False] * (s_len+1)
        dp[s_len] = True
        i = p_len - 1
        while i >= 0:
            if p[i] == '*':
                for j in range(s_len-1,-1,-1):
                    dp[j] = dp[j] or (dp[j+1] and (p[i-1] == '.' or p[i-1] == s[j]))
                i -= 1
            else:
                for j in range(s_len):
                    dp[j] = dp[j+1] and (p[i] == '.' or p[i] == s[j])
                dp[s_len] = False
            i -= 1
            print(dp)
        return dp[0]


    def __init__(self, s, p):
        self.s = s
        self.p = p

    def getAns(self, s, p):
        print(Solution.isMatch(self, s, p))

def main():
    s = "aab"
    p = "c*a*b"
    sl = Solution(s,p)
    sl.getAns(s,p)

if __name__ == '__main__':
    main()