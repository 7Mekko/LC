class Solution:
    def __init__(self,s):
        self.s = s

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        ans = 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                str = s[i:j]
                if str.count(s[j]) == 0 :
                    if (j + 1) == len(s):
                        ans = ans if (ans >= j - i + 1) else (j - i + 1)
                        break
                    continue
                else:
                    ans = ans if (ans >= j - i) else (j - i)
                    break
        return ans

    def getans(self,s):
        print(Solution.lengthOfLongestSubstring(self,s))


def main():
    s = input()
    a = Solution(s)
    a.getans(s)


if __name__ == '__main__':
    main()