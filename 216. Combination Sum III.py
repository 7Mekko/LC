class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(res,tmp,k,j,cnt,n):
            if len(tmp) == k and cnt == n:
                print(tmp,cnt)
                l = tmp.copy()
                res.append(l)
                return
            for i in range(j,9):
                if len(tmp) != 0 and i+1 <= tmp[-1]:
                    continue
                tmp.append(i+1)
                cnt += (i + 1)
                dfs(res,tmp,k,i+1,cnt,n)
                tmp.pop()
                cnt -= (i + 1)
        res = []
        tmp = []
        cnt = 0
        dfs(res,tmp,k,0,cnt,n)
        return res