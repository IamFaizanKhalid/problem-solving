class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        paths = defaultdict(list)

        for a,b in prerequisites:
            paths[a].append(b)


        reachable = [False for _ in range(numCourses)]

        visited = [False for _ in range(numCourses)]

        @cache
        def check_cycle(i):
            if visited[i]:
                return True

            reachable[i] = True

            visited[i] = True

            for adj in paths[i]:
                if check_cycle(adj):
                    return True

            visited[i] = False

            return False

        
        for i in range(numCourses):
            if check_cycle(i): # check cycle
                return False

        return all(reachable)
