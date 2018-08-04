class Node:
	def __init__(self, char):
		self.char = char
		self.children = {}
		self.word_finished = False
		self.counter = 0


class Trie:

	def __init__(self):
		self.root = Node('*')


	def insert(self, word):
		current = self.root

		for character in word:

			if character in current.children:
				current = current.children[character]
				current.counter += 1

			else:

				new_node = Node(character)
				current.children[character] = new_node
				current = new_node
				current.counter += 1

		current.word_finished = True

	def search(self, word):

		if not self.root.children:
			return False

		current = self.root

		for character in word:
			if character in current.children:
				current = current.children[character]
			else:
				return False
		if current.word_finished:
			return True
		return False



if __name__ == '__main__':

	p ass





