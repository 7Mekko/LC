class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isIp(s):
            if len(s) > 1 and s[0] == "0" or len(s) == 0:
                return False
            tmp = int(s)
            if 0 <= tmp <= 255:
                return True
            return False
        def getIp(res,s,n,i,ip,cnt):
            if len(ip) == n + 4 and cnt == 4:
                ip = ip[:n+3]
                if len(res) == 0:
                    res.append(ip)
                    return
                if len(res) > 0 and ip != res[-1]:
                    print(ip,res[-1])
                    res.append(ip)
                    return
            if cnt < 4:
                for j in range(i,i+4):
                    if isIp(s[i:j]):
                        tmp = ip
                        ip += s[i:j]
                        ip += "."
                        cnt += 1
                        getIp(res,s,n,j,ip,cnt)
                        ip = tmp
                        cnt -= 1
        n = len(s)
        res = []
        cnt = 0
        ip = ""
        getIp(res,s,n,0,ip,cnt)
        return res