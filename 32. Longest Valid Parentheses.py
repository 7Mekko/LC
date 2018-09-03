class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_ = 0
        cnt = 0
        stack = []
        s_len = len(s)
        t = [0 for _ in range(s_len)]
        k = 1
        for (i,c) in enumerate(s):
            if c == ')':
                if len(stack) == 0:
                    stack.append((c,i))
                else:
                    if stack[-1][0] == '(':
                        e = stack.pop()
                        t[e[1]] = k
                        t[i] = k
                        k += 1
                        print(e[1],t[e[1]],t[i])
            else:
                stack.append((c,i))
        print(t)
        for v in t:
            if v == 0:
                cnt = 0
            else:
                cnt += 1
                max_ = max(max_,cnt)
        return max_