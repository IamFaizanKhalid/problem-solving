0/5

# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		# if root == None:
		#	 return []

		# return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

		result = []

		stack = [root]
		while len(stack)>0:
			print(stack)
			node = stack.pop()
			if node != None:
				result.append(node.val)
				stack.append(node.right)
				stack.append(node.left) # this is at the top, so this will be the next

		return result
