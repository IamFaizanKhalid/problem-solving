class Solution:
	def totalFruit(self, fruits: List[int]) -> int:
		n = len(fruits)
		if n < 3:
			return n

		b1 = fruits[0]

		i = 1
		while i < n and fruits[i] == b1:
			i += 1

		if i >= n-1:
			return n

		b2 = fruits[i]

		maxRange = i
		start = 0

		while i < n:
			if fruits[i] not in [b1, b2]:
				maxRange = max(maxRange, i - start)
				start = i

				if i+1 < n:
					b1 = fruits[i-1]
					b2 = fruits[i]
					
					x = i-1
					while x >= 0 and fruits[x] in [b1, b2]:
						x -= 1
					start = x + 1

			i += 1
		
		maxRange = max(maxRange, i - start)

		return maxRange
