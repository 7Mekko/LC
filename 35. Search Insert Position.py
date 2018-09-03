class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        if target <= nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        if target == nums[len(nums)-1]:
            return len(nums)-1
        while i < len(nums):
            if nums[i] == target:
                return i
            if nums[i] < target and nums[i+1] > target:
                return i + 1
            i += 1