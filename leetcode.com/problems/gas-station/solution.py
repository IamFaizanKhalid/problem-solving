class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # not enough gas for the route
        if sum(gas)<sum(cost):
            return -1

        s = 0
        g = 0

        for i in range(len(gas)):
            g += gas[i] - cost[i]
            
            if g<0:
                # starting from next, because it is not possible
                # to reach from any station from 0 to i
                s=i+1
                g=0
        
        # if starting from s, there is gas remaining to go to 0,
        # and there is only one possible solution, this is it
        if g>=0:
            return s

        return -1
