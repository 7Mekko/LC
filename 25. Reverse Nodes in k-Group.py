# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = ListNode(0)
        p.next = head
        c = p
        ans = p
        if c.next == None:
            return ans.next
        for i in range(k):
            if c.next == None:
                return ans.next
            c = c.next
        cnt = 0
        while True:
            for i in range(k - 1, 0, -1):
                a = p
                for j in range(cnt * k + i - 1):
                    a = a.next
                b = a.next
                tmp_b = b
                tmp_c = c
                a.next = tmp_b.next
                b.next = tmp_c.next
                c.next = tmp_b
                c = c.next
            cnt += 1
            for i in range(k):
                if c.next == None:
                    return ans.next
                else:
                    c = c.next

    def __init__(self, head, k):
        self.head = head
        self.k = k

    def getAns(self, head, k):
        AA = []
        ans = Solution.reverseKGroup(self,head,k)
        AA.clear()
        while ans != None:
            AA.append(ans.val)
            ans = ans.next
        print(AA)

def main():
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    k = 2
    s = Solution(ptr,k)
    s.getAns(ptr,k)

if __name__ == '__main__':
    main()