# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
		# inorder left -> x
		# postorder right -> x

		if not (inorder and postorder):
			return None

		rootVal = postorder[-1] # last element in postorder is root

		i = inorder.index(rootVal) # index of root in inorder

		# left x right
		# left right x
		# left is same in both cases,
		# in inorder traversal nodes before i are the left nodes
		# so it will be same amount for the postorder too
		return TreeNode(
			rootVal,
			self.buildTree(inorder[:i], postorder[:i]),
			self.buildTree(inorder[i+1:], postorder[i:-1]) # skipping rootVal
		)
