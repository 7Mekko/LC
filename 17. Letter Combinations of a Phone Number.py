class Solution:
    ans = []
    key = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
           ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        Solution.ans.clear()
        if digits == [] or digits == "":
            return Solution.ans
        str_ = ""
        Solution.dfs(self,digits,str_,0)
        return Solution.ans
    '''
    dfs
    '''
    def dfs(self,digits,str,i):
        if i == len(digits):
            Solution.ans.append(str)
            return
        for j in Solution.key[int(digits[i]) - 2]:
            str += j
            Solution.dfs(self,digits,str,i+1)
            str = str[0:len(str)-1]



    def __init__(self, digits):
        self.digits = digits
    def getAns(self, digits):
        print(Solution.letterCombinations(self,digits))
def main():
    digits = "43"
    S = Solution(digits)
    S.getAns(digits)
if __name__ == '__main__':
    main()