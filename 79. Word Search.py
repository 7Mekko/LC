class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def search(board, i, j, k, word, mp):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            if mp[i][j] == 0:
                mp[i][j] = 1
                if search(board, i - 1, j, k + 1, word, mp) or search(board, i + 1, j, k + 1, word, mp) or search(board, i, j - 1, k + 1, word, mp) or search(board, i, j + 1, k + 1, word, mp):
                    return True
                mp[i][j] = 0
            return False

        m = len(board)
        n = len(board[0])
        mp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if search(board, i, j, 0, word, mp):
                    return True
        return False
