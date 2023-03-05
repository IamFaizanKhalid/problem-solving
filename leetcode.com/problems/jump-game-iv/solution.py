class Solution:
	def minJumps(self, arr: List[int]) -> int:
		if len(arr) == 1:
			return 0

		n = len(arr)

		locations = defaultdict(list)
		for i in range(n):
			locations[arr[i]].append(i)

		dp = [float('inf') for _ in range(n)]
		dp[n-1] = 0

		q = deque()
		q.append(n-1)

		while q:
			i = q.popleft()
			if i == 0:
				return dp[0]

			if i-1>=0 and dp[i-1]>dp[i]+1:
				dp[i-1]=dp[i]+1
				q.append(i-1)

			if i+1<n and dp[i+1]>dp[i]+1:
				dp[i+1]=dp[i]+1
				q.append(i+1)

			for j in locations[arr[i]]:
				if j!=i and dp[j]>dp[i]+1:
					dp[j]=dp[i]+1
					q.append(j)
			
			locations[arr[i]].clear()

		return dp[0]
