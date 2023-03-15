# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
		q = [root]

		n = 1
		null = False
		
		while q:
			for node in q[:n]:
				if node:
					if null:
						return False
					q.append(node.left)
					q.append(node.right)
				else:
					null = True
			
			q = q[n:]
			n *= 2

		return True
