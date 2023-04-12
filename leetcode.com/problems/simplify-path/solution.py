class Solution:
	def simplifyPath(self, path: str) -> str:
		dirs = path.split("/")

		stack = []

		for d in dirs:
			if d == "/" or d == "." or d == "":
				continue
			
			if d == "..":
				if len(stack)>0:
					stack.pop()
			else:
				stack.append(d)

		if len(stack) == 0:
			return "/"

		canonical = ""
		for d in stack:
			canonical+="/"+d

		return canonical
