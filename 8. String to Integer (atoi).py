class Solution:
    def __init__(self, str):
        self.str = str

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str_ = ''
        ans = ''
        str = str.lstrip()
        if ((len(str) == 1) and ((str[0] == '-') or (str[0] == '+'))) or (str == ''):
            return 0
        if ((str[0] == '-') or (str[0] == '+')) and (str[0] != str[1]):
            ans += str[0]
            str = str.lstrip(str[0])
            if (str.isdigit()):
                str_ = str
            else:
                for i in range(len(str)):
                    if str[i].isdigit() and (str[i] != ' '):
                        continue
                    else:
                        str_ = str[:i]
                        break
            ans += str_
            ans = ''.join('%s' % id for id in ans)
            try:
                int_ = int(ans)
            except:
                return 0
            else:
                int_ = int(ans)
        else:
            if (str == ''):
                return 0
            if (str[0] == '-') or (str[0] == '+'):
                return 0
            try:
                int(str)
            except:
                try:
                    int(str[0])
                except:
                    return 0
                else:
                    for i in range(len(str)):
                        if str[i].isdigit() and (str[i] != ' '):
                            continue
                        else:
                            str_ = str[:i]
                            break
                ans += str_
                ans = ''.join('%s' %id for id in ans)
                int_ = int(ans)
            else:
                ans += str
                int_ = int(ans)

        if (int_ > 2 ** 31 - 1):
            return 2 ** 31 - 1
        elif (int_ < -2 ** 31):
            return -2**31
        return int_

    def getans(self,str):
        print(Solution.myAtoi(self,str))


def main():
    str = "-1"
    a = Solution(str)
    a.getans(str)


if __name__ == '__main__':
    main()