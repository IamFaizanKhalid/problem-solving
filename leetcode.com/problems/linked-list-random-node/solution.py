# Definition for singly-linked list.
# class ListNode:
#	 def __init__(self, val=0, next=None):
#		 self.val = val
#		 self.next = next
class Solution:

	def __init__(self, head: Optional[ListNode]):
		self.head = head
		l = 0
		while head:
			l += 1
			head = head.next
		self.len = l


	def getRandom(self) -> int:
		i = random.randint(0, self.len-1)

		p = self.head
		while i:
			p = p.next
			i -= 1

		return p.val

		


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
