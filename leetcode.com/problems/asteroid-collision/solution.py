class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)

        ans = []
        
        for s in asteroids:
            if s > 0:
                ans.append(s)
            else:
                destroyed = False

                for i in range(len(ans)-1,-1,-1):
                    if ans[i] >= abs(s):
                        destroyed = True # negative destroyed
                        ans = ans[:i+1] # destroying all in the way

                        if ans[i] == abs(s): # collided with same sized
                            ans = ans[:i] # opposite also destroyed

                        break

                    elif ans[i] > 0: # destroying smaller positive
                        ans = ans[:i]    

                if not destroyed:
                    ans.append(s) # no positive to collide                    

                    
        return ans
