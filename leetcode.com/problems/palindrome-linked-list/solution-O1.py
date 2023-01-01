# Definition for singly-linked list.
# class ListNode:
#	 def __init__(self, val=0, next=None):
#		 self.val = val
#		 self.next = next
class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		i,j = head,head.next
		e = False
		while j is not None:
			if e:
				i=i.next
			j=j.next
			e = not e

		mid = i

		remaining=mid.next
		mid.next=None
		nlist = None

		while remaining is not None:
			cur = remaining
			remaining = remaining.next

			cur.next = nlist
			nlist = cur
 
		#mid.next = nlist

		while nlist is not None:
			if head.val!=nlist.val:
				return False
			head=head.next
			nlist=nlist.next

		return True
