class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                str_ = haystack[i:len(needle) + i]
                if str_ == needle:
                    return i
        return -1
