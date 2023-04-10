class Solution:
	def isValid(self, s: str) -> bool:
		mapping = {'(':')','{':'}','[':']'}

		stack = []

		for c in s:
			if c == '(' or c == '[' or c == '{':
				stack.append(c)
			else:
				if len(stack) == 0:
					return False
					
				x = stack.pop()
				if mapping[x] != c:
					return False

		return len(stack) == 0
