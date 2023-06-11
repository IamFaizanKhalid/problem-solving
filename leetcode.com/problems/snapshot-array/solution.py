class SnapshotArray:

    def __init__(self, length: int):
        self.map = [[0] for _ in range(length)]
        self.len = length
        self.snaps = 0

    def fill_missing(self, index: int) -> None:
        l = len(self.map[index])
        diff = (self.snaps+1) - l
        if diff > 0:
            for _ in range(diff):
                self.map[index].append(self.map[index][l-1])
        

    def set(self, index: int, val: int) -> None:
        self.fill_missing(index)

        self.map[index][self.snaps] = val
        

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps-1
        

    def get(self, index: int, snap_id: int) -> int:
        l = len(self.map[index])
        if snap_id >= l:
            return self.map[index][l-1]

        return self.map[index][snap_id]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
