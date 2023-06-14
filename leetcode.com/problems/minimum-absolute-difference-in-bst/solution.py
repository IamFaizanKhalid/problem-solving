# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.mn = float('INF')
        self.prev = None

        def recurse(node):
            if node is None:
                return

            recurse(node.left)

            if self.prev is not None:
                self.mn = min(self.mn, node.val-self.prev)

            self.prev = node.val

            recurse(node.right)

        recurse(root)

        return self.mn
