class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        h, b, l = 0, 0, 0
        for i in nums:
            if i == 0:
                h += 1
            if i == 1:
                b += 1
            if i == 2:
                l += 1
        for i in range(h):
            nums[i] = 0
        for i in range(h,h+b):
            nums[i] = 1
        for i in range(h+b,h+b+l):
            nums[i] = 2