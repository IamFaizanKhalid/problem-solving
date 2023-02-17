# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def maxInBST(self, root: Optional[TreeNode]) -> int:
		while root.right:
			root=root.right

		return root.val

	def minInBST(self, root: Optional[TreeNode]) -> int:
		while root.left:
			root=root.left

		return root.val


	def minDiffInBST(self, root: Optional[TreeNode]) -> int:
		if not root:
			return float('inf')

		l = r = float('inf')

		if root.left:
			l = min(root.val-self.maxInBST(root.left), self.minDiffInBST(root.left))
		if root.right:
			r = min(self.minInBST(root.right)-root.val, self.minDiffInBST(root.right))

		return min(l,r)
