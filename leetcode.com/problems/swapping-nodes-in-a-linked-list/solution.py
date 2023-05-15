# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        n1 = head
        for i in range(k-1):
            n1 = n1.next

        p1 = head
        p2 = n1

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        n2 = p1

        n1.val, n2.val = n2.val, n1.val

        return head
