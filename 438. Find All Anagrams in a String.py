class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, m = len(s), len(p)
        res = []
        if n < m:
            return res
        v = [0 for _ in range(26)]
        t = [0 for _ in range(26)]
        for i in range(m):
            v[ord(p[i])-97] += 1
            t[ord(s[i])-97] += 1
        for i in range(n-m+1):
            if v == t:
                res.append(i)
            if i < n - m:
                t[ord(s[i])-97] -= 1
                t[ord(s[i+m])-97] += 1
        return res