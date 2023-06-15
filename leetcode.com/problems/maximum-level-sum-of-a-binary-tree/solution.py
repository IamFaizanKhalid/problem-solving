# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        mx = -1000000
        mxLvl = 1

        lvl = 1
        q = [root]

        while q:
            l = len(q)

            sm = 0
            for i in range(l):
                node = q[i]

                sm += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if sm>mx:
                mx=sm
                mxLvl=lvl

            q=q[l:]
            lvl += 1

        return mxLvl
