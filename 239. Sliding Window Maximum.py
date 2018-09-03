class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        q = []
        n = len(nums)
        for i in range(n):
            while(len(q) != 0 and nums[q[-1]] <= nums[i]):
                q.pop()
            q.append(i)
            if q[0] == i - k:
                q.pop(0)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res