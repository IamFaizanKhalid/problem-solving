class Solution:
	def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
		n = len(spells)
		m = len(potions)

		potions.sort()

		def getPotionCount(spell):
			i,j = 0,m

			while i<j:
				mid = (i+j)//2

				if potions[mid]*spell < success:
					i=mid+1
				else:
					j=mid
					
			return m-i

		return [getPotionCount(spell) for spell in spells]
