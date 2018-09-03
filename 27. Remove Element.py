class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        cnt, i = 0, 0
        while i < nums_len:
            if nums[i] == val:
                del nums[i]
                nums_len -= 1
            else:
                cnt += 1
                i += 1
        return cnt
