


class Node(object):

	def __init__(self, data):

		self.data = data
		self.height = 0
		self.left_child = None
		self.right_child = None



class AVL(object):


	def __init__(self):
		self.root = None

	def calc_height(self, node):

		if not node:
			return -1

		return node.height

	def calc_balanced(self, node):

		if not node:
			return 0

		return self.calc_height(node.left_child) - self.calc_height(node.right_child)


'''

	def rotate_right(self, node):

		print(node.data)

		temp_left_child = node.left_child
		t = temp_left_child.right_child

		temp_left_child.right_child = node
		node.left_child = t

		node.height = max(self.calc_height(node.left_child), \
			self.calc_height(node.right_child)) + 1
'''




