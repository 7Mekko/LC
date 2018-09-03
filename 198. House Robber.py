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
        s1 = Next(0,n,nums)
        s2 = Next(1,n,nums)
        return max(s1,s2)