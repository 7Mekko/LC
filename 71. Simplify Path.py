class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tmp = path.split("/")
        res = ["/"]
        for s in tmp:
            if s == "" or s == ".":
                continue
            if s == "..":
                if len(res) == 1:
                    continue
                res.pop()
                res.pop()
                continue
            res.append(s)
            res.append("/")
        if len(res) != 1:
            res.pop()
        p = "".join(res)
        return p