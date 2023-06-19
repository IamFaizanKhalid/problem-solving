class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        sm = 0

        for g in gain:
            sm += g
            alt = max(alt, sm)

        return alt
