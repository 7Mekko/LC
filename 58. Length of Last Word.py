class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        n = len(s)
        if n == 0:
            return 0
        cnt = 0
        i = n - 1
        while i >= 0:
            if s[i] == ' ':
                break
            cnt += 1
            i -= 1
        return cnt