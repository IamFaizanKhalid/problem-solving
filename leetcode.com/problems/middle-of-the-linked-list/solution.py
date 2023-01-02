# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		i,j = head,head
		e = False
		while j is not None:
			if e:
				i=i.next
			j=j.next
			e = not e

		return i
    
