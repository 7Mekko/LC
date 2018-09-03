class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        length = len(nums)
        min_ = 0
        s = 0
        if length <= 1:
            return True
        while(i < length):
            if (i + nums[i] >= length - 1):
                return True
            max_ = 0
            if nums[i] == 0:
                return False
            for j in range(i+1,i+nums[i]+1):
                if max_ < j + nums[j]:
                    s = j
                    max_ = j + nums[j]
            i = s
            min_ += 1
        return True