# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def isSymmetric(self, root: Optional[TreeNode]) -> bool:
		l = root.left
		r = root.right
		if l and r:
			if l.val != r.val:
				return False
			return self.isSymmetric(TreeNode(0, l.left, r.right)) and self.isSymmetric(TreeNode(0, l.right, r.left))
		elif l or r:
			return False
		else:
			return True

		
		# lq = []
		# if root.left:
		#	 lq.append(root.left)
		# rq = []
		# if root.right:
		#	 rq.append(root.right)


		# while lq or rq:
		#	 ls = len(lq)
		#	 rs = len(rq)

		#	 if ls!=rs:
		#		 return False

		#	 for i in range(ls):
		#		 l = lq[i]
		#		 r = rq[i]

		#		 if l and r:
		#			 if l.val != r.val:
		#				 return False
		#		 elif l or r:
		#			 return False
		#		 else:
		#			 continue
				

		#		 lq.append(l.left)
		#		 lq.append(l.right)

		#		 rq.append(r.right)
		#		 rq.append(r.left)

		#	 lq = lq[ls:]
		#	 rq = rq[rs:]

		# return True
