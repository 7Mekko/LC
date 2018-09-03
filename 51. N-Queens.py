class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def solve(x,n,m,ans):
            def judge(x,y,m):
                for j in range(x):
                    if m[j] == y or (abs(x-j) == abs(m[j]-y)):
                        return False
                return True
            if x == n :
                tmp = []
                for i in range(n):
                    j = 1
                    s = ""
                    while j <= n:
                        if m[i] == j:
                            s += "Q"
                        else:
                            s += "."
                        j += 1
                    tmp.append(s)
                ans.append(tmp)
            else:
                for i in range(1,n+1):
                    if judge(x,i,m):
                        m[x] = i
                        solve(x+1,n,m,ans)
        m = [0 for _ in range(n)]
        ans = []
        solve(0,n,m,ans)
        return ans

    def __init__(self, n):
        self.n = n

    def getAns(self, n):
        print(Solution.solveNQueens(self,n))

def main():
    n = 6
    s = Solution(n)
    s.getAns(n)

if __name__ == '__main__':
    main()