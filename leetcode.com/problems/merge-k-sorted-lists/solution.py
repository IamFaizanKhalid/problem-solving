# Definition for singly-linked list.
# class ListNode:
#	 def __init__(self, val=0, next=None):
#		 self.val = val
#		 self.next = next
class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

		pq = []

		for i, lst in enumerate(lists):
			if lst:
				heapq.heappush(pq, (lst.val, i))
				lists[i] = lists[i].next

		if not pq:
			return None


		v, i = heapq.heappop(pq)
		ans = ListNode(v)
		cur = ans
		if lists[i]:
			heapq.heappush(pq, (lists[i].val, i))
			lists[i] = lists[i].next

		while pq:
			v, i = heapq.heappop(pq)
			cur.next = ListNode(v)
			cur = cur.next
			if lists[i]:
				heapq.heappush(pq, (lists[i].val, i))
				lists[i] = lists[i].next
		
		return ans
