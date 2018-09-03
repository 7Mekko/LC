class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        m = n // 3
        from collections import Counter
        dic = Counter(nums)
        print(dic,m)
        for x in dic:
            print(x,dic[x])
            if dic[x] > m:
                res.append(x)
        return res