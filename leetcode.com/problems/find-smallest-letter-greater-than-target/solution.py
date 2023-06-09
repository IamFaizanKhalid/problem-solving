class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l, r = 0, n-1

        while l<=r:
            m = (l+r)//2

            if letters[m]>target:
                r = m-1
            else:
                l = m+1

        return letters[0] if l==n else letters[l]
