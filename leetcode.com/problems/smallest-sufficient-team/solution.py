class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        m = len(req_skills)

        skill_num = {}
        for i in range(m):
            skill_num[req_skills[i]] = i


    
        skills = [0 for _ in range(n)]

        for i in range(n):
            for skill in people[i]:
                skills[i] |= 1 << skill_num[skill]


        @cache
        def f(skills_mask):
            if skills_mask == 0:
                return 0
                
            ans = -1

            for i in range(n):
                new_skills_mask = skills_mask & ~skills[i]

                if new_skills_mask != skills_mask:
                    people_mask = f(new_skills_mask) | (1 << i)

                    if (ans < 0 or people_mask.bit_count() < ans.bit_count()):
                        ans = people_mask

            return ans


        answer_mask = f((1 << m) - 1)

        ans = []
        for i in range(n):
            if (answer_mask >> i) & 1:
                ans.append(i)

        return ans
    
