class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def Next(l,r,nums):
            p, pp = 0, 0
            for i in range(l,r):
                if pp + nums[i] >= p:
                    pp, p = p, pp + nums[i]
                else:
                    pp = p
            return p
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        s1 = Next(0,n-1,nums)
        s2 = Next(1,n,nums)
        return max(s1,s2)
    def __init__(self, nums):
        self.nums = nums

def main():
    nums = [1,2,3,1,1,5,7,5,3,4,8,7,12,3,5,4,8,9,7,4,113,6,7,4,563,2,4,6,8,7,4,134,5,4,8,4,36,1,567,1,523,574,8,1,3,5,8,1,3,4,89,46]
    ss = Solution(nums)
    pp = ss.rob(nums)
    print(pp)
if __name__ == '__main__':
    main()