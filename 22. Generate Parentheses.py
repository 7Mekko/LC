class Solution:
    ans = []
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        Solution.ans.clear()
        str_ = ''
        if n == 0:
            return Solution.ans
        Solution.genP(self,n,n,str_)
        return Solution.ans

    def genP(self, i, j, str):
        if i == 0 and j == 0:
            Solution.ans.append(str)
        if i == 0 and j > 0:
            str += ')'
            Solution.genP(self,i,j-1,str)
        if (i == j and j > 0):
            str += '('
            Solution.genP(self,i-1,j,str)
        if (i < j and i > 0):
            str += '('
            Solution.genP(self,i-1,j,str)
            str = str[0:len(str)-1]
            str += ')'
            Solution.genP(self,i,j-1,str)
    def __init__(self, n):
        self.n = n

    def getAns(self, n):
        print(Solution.generateParenthesis(self, n))

def main():
    n = 9
    gp = Solution(n)
    gp.getAns(n)

if __name__ == '__main__':
    main()