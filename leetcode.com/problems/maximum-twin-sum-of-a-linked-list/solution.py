# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find mid
        mid, end = head, head

        while end:
            mid = mid.next
            end = end.next.next

        # reverse 2nd
        head2 = None
        while mid:
            x = mid.next

            mid.next = head2
            head2 = mid

            mid = x

        # find ans
        mx = 0
        while head2:
            mx = max(mx, head2.val+head.val)
            head = head.next
            head2 = head2.next

        return mx
