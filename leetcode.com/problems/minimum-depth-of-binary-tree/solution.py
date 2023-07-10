# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = [root]

        d = 0
        while q:
            d += 1
            l = len(q)

            for i in range(l):
                node = q[i]

                if node.left or node.right:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    return d

            q = q[l:]

        return d
