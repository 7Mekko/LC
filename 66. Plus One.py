class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp = "".join("%s" % i for i in digits)
        tmp = str(int(tmp) + 1)
        ans = [int(i) for i in tmp]
        return ans