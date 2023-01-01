class Solution(object):
	def romanToInt(self, s):
		vals = {
			'I' : 1,
			'V' : 5,
			'X' : 10,
			'L' : 50,
			'C' : 100,
			'D' : 500,
			'M' : 1000,
		}		 

		v = [vals.get(s[0])]
		i = 1

		while i < len(s):
			v.append(vals.get(s[i]))
			
			if v[i-1] < v[i]:
				v[i-1] =- v[i-1]
			i+=1


		return sum(v)
