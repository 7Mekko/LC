class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def _solveSudoku(board, i, j):
            nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            if i == 9:
                return True
            if j == 9:
                return _solveSudoku(board, i + 1, 0)
            if (board[i][j] != '.'):
                return _solveSudoku(board, i, j + 1)
            for k in range(9):
                val = nums[k]
                if (Solution.check(self, board, i, j, val)):
                    board[i][j] = val
                    if (_solveSudoku(board, i, j + 1)):
                        return True
                    board[i][j] = '.'
            return False

        _solveSudoku(board, 0, 0)

    def check(self, board, i, j, val):
        row, column = i - i % 3, j - j % 3;
        for x in range(9):
            if board[x][j] == val:
                return False
        for y in range(9):
            if board[i][y] == val:
                return False
        for x in range(3):
            for y in range(3):
                if (board[row + x][column + y] == val):
                    return False
        return True