class Solution:
	def minimumRounds(self, tasks: List[int]) -> int:
		# counts = {}

		# for dif in tasks:
		#	 if not dif in counts:
		#		 counts[dif]=1
		#	 else:
		#		 counts[dif]+=1

		rounds= 0

		for dif,count in Counter(tasks).items(): # counts.items():
			if count==1:
				return -1
			twos = count // 2
			threes = 0
			if count % 2 == 1:
				twos-=1
				threes=1
			threes+=(twos//3)*2
			twos%=3
			rounds += threes+twos

		return rounds
