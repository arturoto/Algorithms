
class Node:

	def __init__(self, name):
		self.name = name
		self.adjacentList = []
		self.visited = False;
		self.predecessor = None


class DFS:

	def dfs(self, startNode):

		queue = []
		queue.append(startNode)
		startNode.visited = True


		while queue:

			currentNode = queue.pop()
			print('{}'.format(currentNode.name))


			for n in currentNode.adjacentList:
				if not n.visited:
					n.visited = True
					queue.append(n)

	def dfs_rec(self, currentNode):

		currentNode.visited = True
		print('{}'.format(currentNode.name))

		for n in currentNode.adjacentList:
			if not n.visited:
				self.dfs(n)





root = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')
node_g = Node('g')
node_h = Node('h')


# Connecting 

root.adjacentList.append(node_b)
root.adjacentList.append(node_c)

node_b.adjacentList.append(node_d)
node_b.adjacentList.append(node_e)
node_b.adjacentList.append(node_f)

node_c.adjacentList.append(node_g)
node_g.adjacentList.append(node_h)



dfs = DFS()


# dfs.dfs(root)



dfs.dfs_rec(root)










