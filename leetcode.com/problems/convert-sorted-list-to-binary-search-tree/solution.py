# Definition for singly-linked list.
# class ListNode:
#	 def __init__(self, val=0, next=None):
#		 self.val = val
#		 self.next = next
# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
		if not head:
			return None

		if not head.next:
			return TreeNode(head.val)

		# getting middle node by fast/slow pointers
		beforeMiddle = None
		middle = head
		last = head
		while last and last.next:
			beforeMiddle = middle
			middle = middle.next
			last = last.next.next

		# splitting linked list
		left = head
		beforeMiddle.next = None

		right = middle.next
		middle.next = None

		return TreeNode(middle.val, self.sortedListToBST(left), self.sortedListToBST(right))
