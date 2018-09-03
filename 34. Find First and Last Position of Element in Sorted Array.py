class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l , r = 0 , len(nums) - 1
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
        while l <= r :
            c = (l + r) // 2
            if nums[c] == target:
                l , r = c , c
                while l > 0:
                    if nums[l - 1] == target:
                        l -= 1
                    else:
                        break
                while r < len(nums) - 1:
                    if nums[r + 1] == target:
                        r += 1
                    else:
                        break
                return [l,r]
            elif nums[c] < target:
                l = c + 1
            else:
                r = c - 1
        return [-1,-1]