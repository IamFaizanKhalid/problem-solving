# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#		 self.val = val
#		 self.left = left
#		 self.right = right
class Solution:
	def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
		def recurse(node):
			if not node:
				return 0
			triplet = (recurse(node.left), node.val, recurse(node.right))
			if triplet not in triplet_to_id:
				triplet_to_id[triplet] = len(triplet_to_id) + 1
			id = triplet_to_id[triplet]
			cnt[id] += 1
			if cnt[id] == 2:
				res.append(node)
			return id
		
		triplet_to_id = {}
		cnt = defaultdict(int)
		res = []
		recurse(root)
		return res
