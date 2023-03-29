class Solution:
	def maxSatisfaction(self, satisfaction: List[int]) -> int:
		n = len(satisfaction)

		satisfaction.sort()
		# satisfaction = sorted(satisfaction)

		start = 0
		while start<n and satisfaction[start]<1:
			start += 1
		
		answer=0
		while start>=0:
			total = 0
			multiple = 1
			i = start
			while i<n:
				total += satisfaction[i]*multiple
				i += 1
				multiple += 1

			if total<answer:
				break
			answer = total
			start -= 1

		return answer
