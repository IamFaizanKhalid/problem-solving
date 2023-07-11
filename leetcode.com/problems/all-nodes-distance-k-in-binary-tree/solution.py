# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        NOT_FOUND = -1

        self.ans = []

        def recurse(node, dist):
            if not node:
                return NOT_FOUND

            if dist == k:
                self.ans.append(node.val)

            # target node
            if node.val == target.val:
                if k==0: # k=0 edge case
                    self.ans.append(node.val)

                recurse(node.left, 1)
                recurse(node.right, 1)

                return 1


            # non target node
            
            if dist != NOT_FOUND:
                dist += 1

            leftDist = recurse(node.left, dist)
            rightDist = recurse(node.right, dist)
                
            dist = max(leftDist, rightDist)

            if dist == NOT_FOUND:
                return NOT_FOUND

            if dist == k:
                self.ans.append(node.val)


            if leftDist > 0:
                # target was on left side, going right
                recurse(node.right, dist+1)            
            elif rightDist > 0:
                # target was on right side, going left
                recurse(node.left, dist+1)

            # previous node will have +1 distance
            return dist+1

        
        recurse(root, -1)


        return self.ans
