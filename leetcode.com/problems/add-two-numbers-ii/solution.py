# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def prepend_node(lst: ListNode, node: ListNode) -> ListNode:
            node.next = lst
            return node


        def reverse(l: Optional[ListNode]) -> Optional[ListNode]:
            rl = None
            while l:
                nxt = l.next
                rl = prepend_node(rl, l)
                l = nxt

            return rl

        
        l1 = reverse(l1)
        l2 = reverse(l2)

        ans = None
        rem = 0

        while l1 and l2:
            sm = l1.val + l2.val + rem
            rem = sm // 10
            sm %= 10

            ans = prepend_node(ans, ListNode(sm))

            l1 = l1.next
            l2 = l2.next


        def add_remaining(ans: Optional[ListNode], rem: int, l: Optional[ListNode]):
            while l:
                sm = l.val + rem
                rem = sm // 10
                sm %= 10

                ans = prepend_node(ans, ListNode(sm))

                l = l.next

            return ans, rem

        ans, rem = add_remaining(ans, rem, l1)
        ans, rem = add_remaining(ans, rem, l2)

        if rem:
            ans = prepend_node(ans, ListNode(rem))


        return ans
