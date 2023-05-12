class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        @cache
        def recurse(i):
            if i >= n:
                return 0

            points, brainpower = questions[i]
            
            return max(recurse(i+1), points+recurse(i+1+brainpower))

        return recurse(0)
