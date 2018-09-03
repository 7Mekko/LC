class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            c = (l + r ) // 2
            if nums[c] == target:
                return True
            elif nums[c] < nums[l]:
                if nums[c] < target and target <= nums[r]:
                    l = c + 1
                else:
                    r = c
            elif nums[l] < nums[c]:
                if nums[l] <= target and target < nums[c]:
                    r = c
                else:
                    l = c + 1
            else:
                l += 1
        return False