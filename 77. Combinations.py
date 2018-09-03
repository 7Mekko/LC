class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(res,n,tmp,k,j):
            if len(tmp) == k:
                l = tmp.copy()
                res.append(l)
                return
            for i in range(j,n):
                if len(tmp) != 0 and i+1 <= tmp[-1]:
                    continue
                tmp.append(i+1)
                dfs(res,n,tmp,k,i+1)
                tmp.pop()
        res = []
        tmp = []
        dfs(res,n,tmp,k,0)
        return res