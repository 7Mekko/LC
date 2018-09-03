class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S_len = len(S)
        i = 0
        str_ = ''
        while i<S_len:
            if S[i].isnumeric():
                j = int(S[i]) - 1
                tmp = str_
                while j > 0:
                    str_ += tmp
                    j -= 1
            else:
                str_ += S[i]
            if len(str_) >= K:
                return str_[K-1]
            i += 1


    def __init__(self, S, K):
        self.S = S
        self.K = K
    def getAns(self, S ,K):
        print(Solution.decodeAtIndex(self, S, K))
def main():
    S = "y959q969u3hb22odq595"
    K = 222280369
    ss = Solution(S,K)
    ss.getAns(S,K)

if __name__ == '__main__':
    main()