class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(res, n, nums, tmp, j):
            l = tmp.copy()
            res.append(l)
            for i in range(j, n):
                tmp.append(nums[i])
                dfs(res, n, nums, tmp, i + 1)
                tmp.pop()

        n = len(nums)
        res = []
        tmp = []
        dfs(res, n, nums, tmp, 0)
        return res