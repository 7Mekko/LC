class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        nums.sort()
        nums_len = len(nums)
        for i in range(nums_len-1,0,-1):
            if nums[i] > nums[i-1]:
                count += 1
            if count == 3:
                return nums[i-1]
        return nums[nums_len-1]
        print(nums)

    def __init__(self, nums):
        self.nums = nums

    def getAns(self, nums):
        print(Solution.thirdMax(self, nums))

def main():
    nums = [1, 2, 3, 3,3,3,3,3,2,4 ]
    S = Solution(nums)
    S.getAns(nums)

if __name__ == '__main__':
    main()