class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        def in_circle(circle, point):
            x1,y1,r = circle
            x2,y2,_ = point

            return (x2-x1)**2 + (y2-y1)**2 <= r**2


        in_range = defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                if in_circle(bombs[i], bombs[j]):
                    in_range[i].append(j)
                if in_circle(bombs[j], bombs[i]):
                    in_range[j].append(i)


        def denotate(bomb_num):
            denotated = [False for _ in range(n)]
            denotated[bomb_num] = True

            count = 0

            q = [bomb_num]
            while q:
                l = len(q)
                count += l

                for i in range(l):
                    bomb_num = q[i]
    
                    for nearby in in_range[bomb_num]:
                        if not denotated[nearby]:
                            denotated[nearby] = True
                            q.append(nearby)

                q = q[l:]

            return count

        
        return max(denotate(i) for i in range(n))
