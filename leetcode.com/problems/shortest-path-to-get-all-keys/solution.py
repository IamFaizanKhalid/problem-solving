class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])

        in_bound = lambda i,j: (0 <= i < m) and (0 <= j < n)
        INF = float('inf')

        is_wall = lambda c: c == '#'
        is_lock = lambda c: 'A' <= c <= 'Z'
        is_key = lambda c: 'a' <= c <= 'z'
        key_ch = lambda c: chr(ord(c)+32)



        def find_starting():
            for i in range(m):
                for j in range(n):
                    if grid[i][j]=='@':
                        return i,j 

        i,j = find_starting()


        total_keys = sum(is_key(grid[i][j]) for j in range(n) for i in range(m))

        has_key_for_lock = lambda k, l: k & (1 << ord(l)-65)
        has_key = lambda k, x: k & (1 << ord(x)-97)
        add_key = lambda k, x: k | (1 << ord(x)-97)
        count_keys = lambda k: bin(k).count("1")

        visited = {(i,j, 0)}

        steps = 0

        q = [(i,j, 0)]

        while q:
            l = len(q)

            for f in range(l):
                i,j, keys = q[f]

                c = grid[i][j]

                if is_key(c):
                    keys = add_key(keys, c)

                if count_keys(keys) == total_keys:
                    return steps

                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if (
                        in_bound(x, y) and 
                        not is_wall(grid[x][y]) and
                        not (is_lock(c) and not has_key_for_lock(keys, c)) and
                        (x,y,keys) not in visited
                    ):
                        visited.add((x,y, keys))
                        q.append((x,y, keys))

            q = q[l:]

            steps += 1

        # print(visited)

        return -1
