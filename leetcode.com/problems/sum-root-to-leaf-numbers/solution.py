# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def sumNumbers(self, root: Optional[TreeNode]) -> int:
		def recurse(r, sm):
			if not r:
				return 0

			sm = sm * 10 + r.val

			if r.left or r.right:
				return recurse(r.left, sm) + recurse(r.right, sm)
			else:
				return sm

		return recurse(root, 0)
