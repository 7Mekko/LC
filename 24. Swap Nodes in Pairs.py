# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        p.next = head
        ans = p
        while p.next and p.next.next:
            tmp = p.next
            tmp1 = p.next.next
            tmp.next = tmp1.next
            p.next = tmp1
            tmp1.next = tmp
            p = p.next.next
        ans = ans.next
        return ans