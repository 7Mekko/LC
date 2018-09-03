class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            try:
                nums.index(target - nums[i])
            except:
                continue
            else:
                if i == nums.index(target - nums[i]):
                    continue
                else:
                    return [i, nums.index(target - nums[i])]