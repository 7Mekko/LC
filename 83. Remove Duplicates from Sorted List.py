# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        q = dummy
        m = dummy
        if not p.next:
            return dummy.next
        p = p.next.next
        q = q.next
        while p:
            if q.val != p.val:
                p = p.next
                q = q.next
            else:
                p = p.next
                m = p
                while p and q.val == p.val:
                    p = p.next
                    m = m.next
                    if not p:
                        break
                q.next = m
        return dummy.next