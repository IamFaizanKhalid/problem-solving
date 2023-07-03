class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        chN = lambda c: ord(c) - 95

        # for same strings, checking for repeating charcter in s,
        # which can be swapped to get the same string
        if s == goal:
            count = [0 for _ in range(26)]
            for c in s:
                i = chN(c)
                count[i] += 1
                if count[i] > 1:
                    return True

            return False

        n = len(s)

        diff = 0
        ch_goal, ch_s = '0', '0'

        for i in range(n):
            if s[i] != goal[i]:
                diff += 1
                
                if diff > 1 and (goal[i]!=ch_s or s[i]!=ch_goal):
                    return False
                
                ch_s = s[i]
                ch_goal = goal[i]

                if diff > 2:
                    return False
        
        return diff == 2
