class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, i = 1, 0
        n = len(nums)
        while i < n:
            if i > 0:
                if nums[i] != nums[i - 1]:
                    cnt = 1
                elif nums[i] == nums[i - 1]:
                    if cnt == 1:
                        cnt += 1
                    else:
                        del nums[i]
                        i -= 1
                        n -= 1
            i += 1
        return len(nums)

