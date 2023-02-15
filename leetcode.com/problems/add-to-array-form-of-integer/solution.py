class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)

        i = n-1

        carry = 0

        while i>=0 and k>0:
            num[i] += k%10 + carry

            carry = num[i]//10

            num[i] %= 10

            k = k//10
            i -= 1

        while i>=0 and carry>0:
            num[i] += carry

            carry = num[i]//10

            num[i] %= 10

            i -= 1

        while k>0:
            num = [k%10 + carry] + num

            carry = num[0]//10

            num[0] %= 10

            k = k//10

        if carry>0:
            num = [carry] + num

        return num
