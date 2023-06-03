class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(list)

        for i in range(n):
            subordinates[manager[i]].append(i)

        def inform_subordinates(managerID):
            if managerID not in subordinates:
                return 0

            return (
                informTime[managerID] +
                max(inform_subordinates(subID) for subID in subordinates[managerID])
                )

        return inform_subordinates(headID)

