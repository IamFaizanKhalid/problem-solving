class Solution:
	def minDistance(self, word1: str, word2: str) -> int:

		dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]

		def recurse(word1, word2, i1, i2):
			if i1 < 0:
				return i2+1 # to be removed
			
			if i2 < 0:
				return i1+1 # to be removed

			if dp[i1][i2] == -1:
				if word1[i1] == word2[i2]:
					# skip current
					dp[i1][i2] = recurse(word1, word2, i1-1, i2-1)
				else:
					# insert i2
					insert = recurse(word1, word2, i1, i2-1) 
					# remove i1
					delete = recurse(word1, word2, i1-1, i2)
					# replace
					replace = recurse(word1, word2, i1-1, i2-1)

					# 1 current operation + min
					dp[i1][i2] = 1 + min(insert, delete, replace)

			return dp[i1][i2]

		return recurse(word1, word2, len(word1)-1, len(word2)-1)



		# n1 = len(word1)
		# n2 = len(word2)

		# if n1 == 0:
		#	 return n2
			
		# if n2 == 0:
		#	 return n1

		# dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

		# for i1 in range(1, n1+1):
		#	 dp[i1][0] = i1

		# for i2 in range(1, n2+1):
		#	 dp[0][i2] = i2

		# for i1 in range(1, n1+1):
		#	 for i2 in range(1, n2+1):
		#		 if word2[i2 - 1] == word1[i1 - 1]:
		#			 dp[i1][i2] = dp[i1 - 1][i2 - 1]
		#		 else:
		#			 dp[i1][i2] = 1+min(dp[i1-1][i2], dp[i1][i2-1], dp[i1-1][i2-1])

		# return dp[n1][n2]
