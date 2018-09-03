class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(res, n, nums, tmp, j):
            l = tmp.copy()
            try:
                res.index(l)
            except:
                res.append(l)
            for i in range(j, n):
                tmp.append(nums[i])
                dfs(res, n, nums, tmp, i + 1)
                tmp.pop()

        n = len(nums)
        nums.sort()
        res = []
        tmp = []
        dfs(res, n, nums, tmp, 0)
        return res