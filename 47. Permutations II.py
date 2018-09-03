class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def _permuteUnique(nums, k, n, ans):
            if k == n and ans.count(nums) == 0:
                ans.append(nums)
            else:
                for j in range(k, n + 1):
                    if nums[j] == nums[k]:
                        num = nums.copy()
                        _permuteUnique(num, j + 1, n, ans)
                        continue
                    else:
                        tmp = nums[j]
                        nums[j] = nums[k]
                        nums[k] = tmp
                        num = nums.copy()
                        _permuteUnique(num, k + 1, n, ans)
                        tmp = nums[j]
                        nums[j] = nums[k]
                        nums[k] = tmp
        ans = []
        i = 0
        l = len(nums) - 1
        _permuteUnique(nums, i, l, ans)
        return ans