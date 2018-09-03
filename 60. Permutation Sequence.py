class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ""
        num = []
        for i in range(n):
            num.append(i+1)
        f = [1 for _ in range(n)]
        for i in range(1,n):
            f[i] = f[i-1] * i
        print(f)
        k -= 1
        for i in range(n,0,-1):
            j = k // f[i-1]
            k %= f[i-1]
            res += str(num[j])
            del num[j]
        return res