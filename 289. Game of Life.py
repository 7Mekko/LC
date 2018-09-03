class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        def count(board,i,j):
            def islegal(board,i,j):
                m = len(board)
                n = len(board[0])
                if i < 0 or i >= m or j < 0 or j >= n:
                    return False
                else:
                    return True
            cnt = 0
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if k == i and l == j:
                        continue
                    if islegal(board,k,l):
                        if board[k][l] == 1 or board[k][l] == -1:
                            cnt += 1
            return cnt
        m = len(board)
        n = len(board[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                cnt = count(board,i,j)
                if board[i][j] == 1:
                    if cnt < 2  or cnt > 3:
                        board[i][j] = -1
                if board[i][j] == 0:
                    if cnt == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1