# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def longestZigZag(self, root: Optional[TreeNode]) -> int:
		dp = {}
		def path(node, d): # d -> 0 left, 1 right
			if not node:
				return 0

			if (node,d) not in dp:
				l = 1

				if d == 0:
					l += path(node.left, 1)
				else:
					l += path(node.right, 0)
				
				dp[(node,d)] = l
			
			return dp[(node,d)]

		def findMax(node):
			if not node:
				return 0
	
			cur = max(path(node,0),path(node,1))

			child = max(findMax(node.left),findMax(node.right))

			return max(cur,child)

		return findMax(root)-1
