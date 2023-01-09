# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		result = []

		stack = [root]
		while len(stack)>0:
			node = stack.pop()
			if node != None:
				if node.left==None and node.right==None:
					result.append(node.val)
				else:
					stack.append(TreeNode(val=node.val))
					stack.append(node.right)
					stack.append(node.left)

		return result
