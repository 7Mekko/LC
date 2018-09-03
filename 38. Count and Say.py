class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        ss = '1'
        i = 1
        while i < n:
            str_ = ''
            cnt = 0
            tmp = ''
            for s in ss:
                if s != tmp and cnt != 0:
                    str_ += str(cnt)
                    str_ += tmp
                    tmp = s
                    cnt = 1
                    continue
                else:
                    cnt += 1
                    tmp = s
            str_ += str(cnt)
            str_ += tmp
            ss = str_
            i += 1
        return ss


