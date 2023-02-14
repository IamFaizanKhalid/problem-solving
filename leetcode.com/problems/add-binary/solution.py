class Solution:
    def addBinary(self, a: str, b: str) -> str:
        minS = min(a,b, key=len)
        maxS = max(a,b, key=len)

        def add(x,y,c):
            x = ord(x)-48
            y = ord(y)-48
            t = x+y+c
            return t//2, chr(t%2+48)

        result = ""
        carry = 0
        for i in range(len(minS)):
            carry, ans = add(a[len(a)-1-i], b[len(b)-1-i], carry)
            result = ans + result

        for i in range(len(maxS)-len(minS)-1, -1, -1):
            carry, ans = add(maxS[i], '0', carry)
            result = ans + result

        return result if carry==0 else chr(carry+48)+result
            

        # return format(int(a,2)+int(b,2), 'b')
