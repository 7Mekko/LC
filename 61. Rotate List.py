# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = head
        cnt = 1
        while dummy.next:
            cnt += 1
            dummy = dummy.next
        k = cnt - k % cnt
        #尾结点连接头结点
        dummy.next = head
        while k != 0:
            dummy = dummy.next
            k -= 1
        #断开
        head = dummy.next
        dummy.next = None
        return head