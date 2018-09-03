class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        n = len(nums)
        m = n // 2
        from collections import Counter
        dic = Counter(nums)
        for x in dic:
            if dic[x] > m:
                res.append(x)
        return res[0]