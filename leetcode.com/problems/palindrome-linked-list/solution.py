# Definition for singly-linked list.
# class ListNode(object):
#	 def __init__(self, val=0, next=None):
#		 self.val = val
#		 self.next = next
class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""

		arr = []
		while head is not None:
			arr.append(head.val)
			head = head.next

		i = 0;
		j = len(arr)-1;

		while i<j:
			if arr[i]!=arr[j]:
				return False
			i+=1
			j-=1

		return True
