'''
Look into

import heapq

for python implimentation
'''

class Heap(object):

	HEAP_SIZE = 10

	def __init__(self):
		self.heap = [0]*self.HEAP_SIZE
		self.current_position = -1


	def insert(self, item):

		if self.is_full():
			print('heap is full')

			return
		self.current_position += 1

		self.heap[self.current_position] = item

		self.fix_up(self.current_position)


	def fix_up(self, index):

		parent_index = int((index-1)/2)

		while parent_index >= 0 and self.heap[parent_index] < self.heap[index]:

			temp = self.heap[index]
			self.heap[index] = self.heap[parent_index]
			self.heap[parent_index] = temp
			parent_index = int((index-1)/2)

	def heapsort(self):

		for i in range(0, self.current_position + 1):
			temp = self.heap[0]
			print(temp)
			self.heap[0] = self.heap[self.current_position - i]
			self.heap[self.current_position - i] = temp
			self.fix_down(0, self.current_position - i - 1)

	def fix_down(self, index, upto):

		while index <= upto:
			left_child = 2*index + 1
			right_child = 2*index + 2

			if left_child < upto:
				child_to_swap = None

				if right_child > upto:
					child_to_swap = left_child
				else:
					if self.heap[left_child] > self.heap[right_child]:
						child_to_swap = left_child
					else:
						child_to_swap = right_child
				if self.heap[index] < self.heap[child_to_swap]:
					temp = self.heap[index]
					self.heap[index] = self.heap[child_to_swap]
					self.heap[child_to_swap] = temp
				else:
					break

				index = child_to_swap

			else:
				break


	def is_full(self):
		if self.current_position == Heap.HEAP_SIZE:
			return True

		else:

			return False





if __name__ == '__main__':

	heap = Heap()
	heap.insert(1)

	heap.heapsort()










































