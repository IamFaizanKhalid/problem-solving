class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # index of char
        cN = lambda c: ord(c)-97
        
        lst = [set() for _ in range(26)]
        for idea in ideas:
            start, word = cN(idea[0]), idea[1:]

            lst[start].add(word)


        count = 0
        for i in range(25):
            for j in range(i + 1, 26):
                # common endings count for char i and j
                common = len(lst[i].intersection(lst[j]))

                # uncommon endings count for char i and j
                onlyInI = len(lst[i]) - common
                onlyInJ = len(lst[j]) - common
                
                # these chars can be swapped for uncommon endings
                # *2 to add both (a,b) and (b,a)
                count += 2 * onlyInI * onlyInJ
        
        return count
