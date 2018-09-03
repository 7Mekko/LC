class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        cnt , i = 0 , 0
        while i < nums_len:
            if i == 0:
                i += 1
                cnt += 1
                continue
            if nums[i] == nums[i-1]:
                del nums[i]
                nums_len -= 1
            else:
                cnt += 1
                i += 1
        return cnt