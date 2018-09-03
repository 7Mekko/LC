class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isInt(s):
            if len(s) == 0:
                return False
            for i in range(len(s)):
                if i == 0:
                    if (len(s) != 1 and (s[i] == '+' or s[i] == '-')) or s[i].isnumeric():
                        continue
                    else:
                        return False
                elif (not s[i].isnumeric()):
                    return False
            return True

        def isFloat(s):
            if len(s) == 0 or s == '.' or s == '+.' or s == '-.':
                return False
            flag = 0
            for i in range(len(s)):
                if i == 0 and (s[i] == '+' or s[i] == '-') and len(s) != 1:
                    continue
                if not s[i].isnumeric():
                    if s[i] == '.' and not flag:
                        flag += 1
                    else:
                        return False
            return True

        s = s.lstrip()
        s = s.rstrip()
        n = len(s)
        if n == 0:
            return False
        if isFloat(s) or isInt(s):
            return True
        else:
            for i in range(n):
                if s[i] == 'e' and isFloat(s[:i]) and isInt(s[i + 1:]):
                    print(s[:i], s[i + 1:])
                    return True
            return False
