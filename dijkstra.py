
'''
------------------------>>> DOES NOT WORK!!!!

class Node:


	name
	min_distance
	Node Predecessor



class dijkstra:

	### initialization phase

	distance[source] = 0 
	create vertex queue Q


	for v in graph
		distance[v] = inf # a guess
		predecessor[v] = undefined # previous node in the shortest path
		add v to 

	#########



	while q not empty:
		u = vertext in Q with min disance // this is why we use heaps
		remove v from Q



		# is there a shorter path?
		for each neighbor v of u
		tempDist = distance[u] + distBetween(u,v)
		if tempDist < distance[v]:
			distance[v] = tempDist
			predecessor[v] = u
	return distance[] 


'''

import sys
import heapq

class Edge(object):

	def __init__(self, weight, startVertex, targetVertex):
		self.weight = weight
		self.startVertex = startVertex
		self.targetVertex = targetVertex


class Node(object):

	def __init__(self, name):
		self.name = name
		self.visited = False
		self.predecessor = None
		self.adj = []
		self.minDistance = sys.maxsize # min distance from the starting vertex


	def __cmp__(self, otherVertex):
		return self.cmp(self.minDistance, otherVertex.minDistance)


	def __lt__(self, other):
		selfPriority = self.minDistance
		otherPriority = other.minDistance
		return selfPriority < otherPriority



class Alg(object):

	def shortestPath(self, vertextList, startVertex):

		q = []
		startVertex.minDistance = 0
		heapq.heappush(q, startVertex)


		while  q:
			currentVertex = heapq.heappop(q)

			for edge in currentVertex.adj:
				u = edge.startVertex
				v = edge.startVertex
				newDistance = u.minDistance + edge.weight

				if newDistance < v.minDistance:
					v.predecessor = u
					v.minDistance = newDistance
					heapq.heappush(q, v)

	def getShortestPath(self, targetVertex):
		print('shortest path to vertex is: ', targetVertex.minDistance)

		node = targetVertex

		while node is not None:
			print('%s ' % node.name)
			node = node.predecessor




if __name__ == '__main__':


	node1 = Node('A')
	node2 = Node('B')
	node3 = Node('C')
	node4 = Node('D')
	node5 = Node('E')
	node6 = Node('F')
	node7 = Node('G')
	node8 = Node('H')


	edge1 = Edge(5, node1, node2)
	edge2 = Edge(8, node1, node8)
	edge3 = Edge(9, node1, node5)
	edge4 = Edge(15, node2, node4)
	edge5 = Edge(12, node2, node3)
	edge6 = Edge(4, node2, node8)
	edge7 = Edge(7, node8, node3)
	edge8 = Edge(6, node8, node6)
	edge9 = Edge(5, node5, node8)
	edge10 = Edge(4, node5, node6)
	edge11 = Edge(20, node5, node7)
	edge12 = Edge(1, node6, node3)
	edge13 = Edge(13, node6, node7)
	edge14 = Edge(9, node3, node4)
	edge15 = Edge(11, node3, node7)
	edge16 = Edge(9, node4, node7)


	node1.adj.append(edge1)
	node1.adj.append(edge2)
	node1.adj.append(edge3)
	node2.adj.append(edge4)
	node2.adj.append(edge5)
	node2.adj.append(edge6)
	node8.adj.append(edge7)
	node8.adj.append(edge8)
	node5.adj.append(edge9)
	node5.adj.append(edge10)
	node5.adj.append(edge11)
	node6.adj.append(edge12)
	node6.adj.append(edge13)
	node3.adj.append(edge14)
	node3.adj.append(edge15)
	node4.adj.append(edge16)


	vertexList = (node1,node2, node3, node4, node5, node6, node7, node8)

	edgeList = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, \
			edge9, edge10, edge11, edge12, edge13, edge14, edge15, edge16)


	algo = Alg()
	algo.shortestPath(vertexList, node1)
	algo.getShortestPath(node4)




























