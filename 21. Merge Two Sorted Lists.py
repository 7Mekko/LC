# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        ans = dummy
        while l1 or l2:
            while l1 and l2:
                a = l1.val
                b = l2.val
                if a < b:
                    ans.next = ListNode(a)
                    ans = ans.next
                    l1 = l1.next
                else:
                    ans.next = ListNode(b)
                    ans = ans.next
                    l2 = l2.next
            while l1:
                ans.next = ListNode(l1.val)
                ans = ans.next
                l1 = l1.next
            while l2:
                ans.next = ListNode(l2.val)
                ans = ans.next
                l2 = l2.next
        ans = dummy.next
        del dummy
        return ans