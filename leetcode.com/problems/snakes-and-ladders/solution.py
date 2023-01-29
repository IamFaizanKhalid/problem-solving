class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        finish = n*n

        def getTarget(x):
            r = n-1 - ((x-1)//n)
            c = (x-1)%n
            if n%2 == r%2:
                c = n-1-c
            
            return board[r][c] if board[r][c] > -1 else x

        def getNexts(x):
            return [getTarget(x+i) for i in range(1,7) if x+i <= finish]

        distance = [float('inf') for _ in range(finish+1)]

        q = []
        q.append((1, 0)) # (cell, moves)

        while q:
            cell, moves = q.pop(0)
            
            if distance[cell] > moves:
                distance[cell] = moves

                q += [(nxt, moves+1) for nxt in getNexts(cell)]

        moves = distance[finish]

        return moves if moves != float('inf') else -1
