# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        list = []
        for l in lists:
            while l:
                list.append(l.val)
                l = l.next
        list.sort()
        dummy = ListNode(0)
        ans = dummy
        for val in list:
            ans.next = ListNode(val)
            ans = ans.next
        ans = dummy.next
        del dummy
        return ans