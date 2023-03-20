class Solution:
	def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
		l = len(flowerbed)

		if l==1:
			total = 1-flowerbed[0]
			return total >= n

		total = 0
		if flowerbed[0]==0 and flowerbed[1]==0:
				flowerbed[0] = 1
				total += 1
		for i in range(1, l-1):
			if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
				flowerbed[i] = 1
				total += 1
		if flowerbed[l-2]==0 and flowerbed[l-1]==0:
				flowerbed[l-1] = 1
				total += 1

		return total >= n
