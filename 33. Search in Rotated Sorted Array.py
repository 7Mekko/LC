class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            c = (l + r) // 2
            if nums[c] == target:
                return c
            elif nums[c] < nums[r]:
                if nums[c] < target and target <= nums[r]:
                    l = c + 1
                else:
                    r = c - 1
            else:
                if nums[l] <= target and target < nums[c]:
                    r = c - 1
                else:
                    l = c + 1
        return -1
