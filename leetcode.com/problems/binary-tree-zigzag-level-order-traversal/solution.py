# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		ans = []

		q = []
		if root:
			q.append(root)

		goLeft = True

		while q:
			n = len(q)
			
			if goLeft:
				ans.append([q[i].val for i in range(n-1,-1,-1)])
			else:
				ans.append([q[i].val for i in range(n)])

			for i in range(n):
				node = q[i]
				if node.right:
					q.append(node.right)
				if node.left:
					q.append(node.left)

			q = q[n:]

			goLeft = not goLeft

		return ans
