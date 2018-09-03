class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def _permute(nums, k, n, ans):
            if k == n:
                ans.append(nums)
            else:
                for j in range(k, n + 1):
                    tmp = nums[j]
                    nums[j] = nums[k]
                    nums[k] = tmp
                    num = nums.copy()
                    _permute(num, k + 1, n, ans)
                    tmp = nums[j]
                    nums[j] = nums[k]
                    nums[k] = tmp

        ans = []
        i = 0
        l = len(nums) - 1
        _permute(nums, i, l, ans)
        return ans
