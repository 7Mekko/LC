class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        max_ = -sys.maxsize - 1
        tmp = 0
        for i in range(len(nums)):
            if tmp < 0:
                tmp = 0
            tmp += nums[i]
            max_ = max(max_,tmp)
        return max_