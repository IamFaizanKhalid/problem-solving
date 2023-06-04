class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)


        visited = [False for _ in range(n)]

        def explore_province(cur_city):
            if visited[cur_city]:
                return

            visited[cur_city] = True

            for city, connected in enumerate(isConnected[cur_city]):
                if connected:
                    explore_province(city)
            


        provinces = 0

        for city in range(n):
            if not visited[city]:
                provinces += 1
                explore_province(city)

        return provinces
