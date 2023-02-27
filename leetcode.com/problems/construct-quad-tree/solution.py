
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> Node:

        def getQuadTree(x, y, size) -> Node:
            if size == 1:
                return Node(grid[x][y] == 1, True, None, None, None, None)
            
            newSize = size // 2

            topLeft = getQuadTree(x,y, newSize)
            topRight = getQuadTree(x,y+newSize, newSize)
            bottomLeft = getQuadTree(x+newSize,y, newSize)
            bottomRight = getQuadTree(x+newSize,y+newSize, newSize)

            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val and topRight.val == bottomLeft.val and bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True, None, None, None, None)

            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        

        return getQuadTree(0,0,len(grid))

