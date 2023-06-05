class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        p1, p2 = coordinates[:2]
        x1,y1 = p1
        x2,y2 = p2

        for x3,y3 in coordinates[2:]:
            # slop of p1 and p2 = slop of p2 and p3
            if (y2-y1)*(x3-x2) != (x2-x1)*(y3-y2): 
                return False

        return True
      
