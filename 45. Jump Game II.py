class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        length = len(nums)
        min_ = 0
        s = 0
        if length <= 1:
            return 0
        while(i < length):
            if (i + nums[i] >= length - 1):
                return min_ + 1
            max_ = 0
            for j in range(i+1,i+nums[i]+1):
                if max_ < j + nums[j]:
                    s = j
                    max_ = j + nums[j]
            i = s
            min_ += 1
        return min_