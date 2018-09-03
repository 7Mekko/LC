# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while(l1 or l2):
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            s += carry
            carry = s // 10
            curr.next = ListNode(s%10)
            curr = curr.next
        if carry == 1:
            curr.next = ListNode(carry)
        curr = dummy.next
        del dummy
        return curr