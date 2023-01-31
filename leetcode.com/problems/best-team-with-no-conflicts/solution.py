class Solution:
	def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
		n = len(ages)
		
		# sorting according to score and then ages if score is equal
		score_age = sorted(zip(scores,ages))


		total = [s for s, _ in score_age]

		# bottom up
		for j in range(1, n):
			for i in range(j):
				if score_age[j][1] >= score_age[i][1]:
					total[j] = max(total[j], total[i]+score_age[j][0])

		return max(total)
