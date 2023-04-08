"""
# Definition for a Node.
class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
	def cloneGraph(self, node: 'Node') -> 'Node':
		if node == None:
			return None

		mapping = {}

		def newGraph(node):
			if node in mapping:
				return mapping[node]
			
			newNode = Node(node.val)
			mapping[node] = newNode

			for neighbor in node.neighbors:
				newNode.neighbors.append(newGraph(neighbor))

			return newNode

		return newGraph(node)
