class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1[0] == '0' or num2[0] == '0':
            return "0"
        l1 = len(num1)
        l2 = len(num2)
        arr = [0 for _ in range(l1+l2)]
        ans = ''
        for i in range(l1-1,-1,-1):
            for j in range(l2-1,-1,-1):
                id1 = i + j
                id2 = i + j + 1
                sum = int(num1[i]) * int(num2[j]) + arr[id2]
                arr[id1] += sum // 10
                arr[id2] = sum % 10
        for v in arr:
            if len(ans) != 0 or v != 0:
                ans += str(v)
        return ans