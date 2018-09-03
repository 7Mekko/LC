class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a,b = list(a),list(b)
        a.reverse()
        b.reverse()
        if len(a) < len(b):
            a , b = b , a
        n = len(b)
        m = len(a)
        carry = 0
        res = []
        for i in range(n):
            if a[i] != b[i]:
                if carry == 0 :
                    res.append(1)
                else:
                    res.append(0)
            elif a[i] == b[i]:
                if a[i] == "0":
                    res.append(carry)
                    carry = 0
                else:
                    res.append(carry)
                    carry = 1
        for i in range(n,m):
            tmp = int(a[i])
            if carry == 0:
                res.append(tmp)
            else:
                if tmp == 1:
                    res.append(0)
                else:
                    res.append(1)
                    carry = 0
        if carry == 1:
            res.append(1)
        res.reverse()
        ans = "".join("%s" % id for id in res)
        return ans