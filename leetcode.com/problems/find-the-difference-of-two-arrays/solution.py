class Solution:
	def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
		t1 = {}
		for n in nums1:
			t1[n] = True

		t2 = {}
		for n in nums2:
			t2[n] = True

		l1 = []
		for n in t1:
			if n not in t2:
				l1.append(n)
		 
		l2 = []
		for n in t2:
			if n not in t1:
				l2.append(n)

		return [l1,l2]
