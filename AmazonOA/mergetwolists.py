"""
# Definition for a Node.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head= n = ListNode(0)
        while l1 and l2:
            if l1.val<=l2.val:
                n.next=l1
                l1=l1.next
            else:
                n.next=l2
                l2=l2.next
            n=n.next
        n.next=l1 or l2
        return head.next
    



