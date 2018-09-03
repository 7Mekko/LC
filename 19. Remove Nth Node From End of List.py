# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n+1):
            first = first.next
        '''
        多走n+1步，等first到头的时候，second刚好到n结点
        '''
        while first != None:
            first = first.next
            second = second.next
        d = second.next
        second.next = d.next
        return dummy.next
