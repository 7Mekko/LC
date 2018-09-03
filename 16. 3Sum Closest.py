class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums_len = len(nums)
        nums.sort()
        sum = 0
        if nums_len <= 3:
            for i in range(nums_len):
                sum += nums[i]
            return sum
        cloest = abs(nums[0] + nums[1] + nums[2] - target)
        best = nums[0] + nums[1] + nums[2]
        for i in range(nums_len):
            l = i + 1
            r = nums_len - 1
            while(l < r):
                sum = nums[i] + nums[l] + nums[r]
                tmp = abs(sum - target)
                if tmp <= cloest:
                    cloest = tmp
                    best = sum
                if sum == target:
                    return target
                elif sum < target:
                    l += 1
                else:
                    r -= 1
        return best


    def __init__(self, nums ,target):
        self.nums = nums
        self.target = target

    def getAns(self, nums, target):
        print(Solution.threeSumClosest(self, nums, target))

def main():
    nums = [6, -18, -20, -7, -15, 9, 18, 10, 1, -20, -17, -19, -3, -5, -19, 10, 6, -11, 1, -17, -15, 6, 17, -18, -3, 16, 19,
     -20, -3, -17, -15, -3, 12, 1, -9, 4, 1, 12, -2, 14, 4, -4, 19, -20, 6, 0, -19, 18, 14, 1, -15, -5, 14, 12, -4, 0,
     -10, 6, 6, -6, 20, -8, -6, 5, 0, 3, 10, 7, -2, 17, 20, 12, 19, -13, -1, 10, -1, 14, 0, 7, -3, 10, 14, 14, 11, 0,
     -4, -15, -8, 3, 2, -5, 9, 10, 16, -4, -3, -9, -8, -14, 10, 6, 2, -12, -7, -16, -6, 10]
    target = -52
    sc = Solution(nums,target)
    sc.getAns(nums,target)
if __name__ == '__main__':
    main()