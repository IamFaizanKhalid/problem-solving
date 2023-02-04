class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		l1, l2 = len(s1), len(s2)
		if l2 < l1:
			return False

		cN = lambda c: ord(c)-97


		# frequency of chars in s1
		ch1Count = [0 for _ in range(26)]
		for c in s1:
			ch1Count[cN(c)] += 1

		# frequency of chars in s2 first slice of length l1
		ch2sCount = [0 for _ in range(26)]
		for c in s2[:l1]:
			ch2sCount[cN(c)] += 1

		# number of characters in both with same frequency
		sameFreqCount = 0
		for i in range(26):
			if ch1Count[i] == ch2sCount[i]:
				sameFreqCount += 1

		# all charcters has same frequency, it's a permutation
		if sameFreqCount == 26:
			return True

		# moving s2 slice to exlude first charcter and include next
		for i in range(0, l2-l1):
			chRem = cN(s2[i])
			ch2sCount[chRem] -= 1

			# after excluding c if its freq has become equal to freq in s1,
			# we have one more c with same freq as in s1
			if ch2sCount[chRem] == ch1Count[chRem]:
				sameFreqCount += 1
			# if its freq has become one less than freq in s1 after -1,
			# we have lost one c with same freq as in s1
			elif ch2sCount[chRem] == ch1Count[chRem] - 1:
				sameFreqCount -= 1
			
			chAdd = cN(s2[i+l1])
			ch2sCount[chAdd] += 1

			# after including c if its freq has become equal to freq in s1,
			# we have one more c with same freq as in s1
			if ch2sCount[chAdd] == ch1Count[chAdd]:
				sameFreqCount += 1
			# if its freq has become one more than freq in s1 after +1,
			# we have lost one c with same freq as in s1
			elif ch2sCount[chAdd] == ch1Count[chAdd] + 1:
				sameFreqCount -= 1

			# checking if current s2 slice has same freq as s1 for all c
			if sameFreqCount == 26:
				return True
		
		return False

