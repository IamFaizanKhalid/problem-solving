class Solution:
	def ways(self, pizza: List[str], k: int) -> int:
		rows = len(pizza)
		cols = len(pizza[0])

		dp = {}
	
		def hasApple(ib,ie,jb,je):
			key = (ib,ie,jb,je)

			if key in dp:
				return dp[(ib,ie,jb,je)]

			for i in range(ib, ie+1):
				for j in range(jb, je+1):
					if pizza[i][j] == 'A':
						dp[key]=True
						return True 

			dp[key]=False
			return False

		
		dp2 = {}

		def maxMethods(ib,jb,k):
			if (ib,jb,k) in dp2:
				return dp2[(ib,jb,k)]

			if not hasApple(ib, rows-1, jb, cols-1):
				return 0

			if k == 1:
				return 1

			total = 0

			for ie in range(ib+1, rows):
				if hasApple(ib, ie-1, jb, cols-1):
					total += maxMethods(ie, jb, k-1)

			for je in range(jb+1, cols):
				if hasApple(ib, rows-1, jb, je-1):
					total += maxMethods(ib, je, k-1)

			dp2[(ib,jb,k)] = total
			
			return total 


		modulo = (10**9)+7

		return maxMethods(0,0,k) % modulo
