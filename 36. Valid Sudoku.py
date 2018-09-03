class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def _isValidSudoku(a, b, board):
            for i in range(9):
                if i == a:
                    continue
                if board[a][b] == board[i][b]:
                    return False
            for i in range(9):
                if i == b:
                    continue
                if board[a][b] == board[a][i]:
                    return False
            k , l = a // 3 , b // 3
            for i in range(k*3,(k+1)*3):
                for j in range(l*3,(l+1)*3):
                    #print(board[i][j])
                    if a == i and b == j:
                        continue
                    if board[a][b] == board[i][j]:
                        return False
            return True
        ans = True
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                ans = _isValidSudoku(i,j,board)
                if ans == False:
                    return ans
        return ans