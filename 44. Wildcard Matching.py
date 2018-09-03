class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p_len = len(p)
        s_len = len(s)
        dp = [[False for _ in range(s_len+1)] for _ in range(p_len+1)]
        dp[0][0] = True
        for i in range(1,p_len+1):
            dp[i][0] = dp[i-1][0] and p[i-1] == '*'
            for j in range(1,s_len+1):
                if p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] and (p[i-1] == '?' or p[i-1] == s[j-1])
        return dp[p_len][s_len]