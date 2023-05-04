class Solution:
	def predictPartyVictory(self, senate: str) -> str:
		n = len(senate)

		r = deque()
		d = deque()
		for i,s in enumerate(senate):
			if s == 'R':
				r.append(i)
			if s == 'D':
				d.append(i)
		
		while r and d:
			if r[0]<d[0]:
				d.popleft()
				r.append(r.popleft()+n)
			else:
				r.popleft()
				d.append(d.popleft()+n)

		return "Radiant" if r else "Dire"
