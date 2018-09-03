class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        '''
        1.strs为空or内容为空
        2.strs长度为1
        3.strs中有一个""
        '''
        if strs == [] or strs == [""]:
            return ''
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs)):
            if strs[i] == "":
                return strs[i]
        str = strs[0]
        for i in range(len(str)):
            str_ = str[0:i+1]
            for j in range(len(strs)):
                if strs[j].find(str_) != 0:
                    str_ = str[0:i]
                    if str_ == None:
                        str_ = ""
                    return str_
        return str_


    def __init__(self, strs):
        self.strs = strs

    def getAns(self, strs):
        print(Solution.longestCommonPrefix(self, strs))

def main():
    strs = ["c","c"]
    s = Solution(strs)
    s.getAns(strs)

if __name__ == '__main__':
    main()