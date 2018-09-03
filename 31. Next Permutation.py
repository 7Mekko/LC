class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 2:
            nums.reverse()
            return
        i = len(nums)-1
        while(nums[i] <= nums[i-1]):
            i -= 1
        if i == 0:
            nums.sort()
            return
        t = i - 1
        p = t + 1
        min_ = nums[t+1] - nums[t]
        for i in range(t+1,len(nums)):
            tmp = nums[i] - nums[t]
            if tmp > 0 and tmp <= min_:
                min_ = tmp
                p = i
        nums[t] , nums[p] = nums[p] , nums[t]
        nums_part_sorted = sorted(nums[t+1:])
        nums[t+1:] = nums_part_sorted