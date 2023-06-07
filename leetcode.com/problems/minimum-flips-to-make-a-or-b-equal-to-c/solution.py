class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0

        while a or b:
            sm = int(a&1) + int(b&1)
            if c&1:
                count += (sm == 0)
            else:
                count += sm

            a = a >> 1
            b = b >> 1
            c = c >> 1

        while c:
            count += c&1
            c = c >> 1

        return count
