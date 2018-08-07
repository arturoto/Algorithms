

def counting_sort(nums, max, min):

	counting_array = [0]*(max - min + 1)

	for i in nums:

		counting_array[i] += 1

	z = 0 

	for i in nums:

		while counting_array[i-min] > 0:

			nums[z] = i 

			z += 1

			counting_array[i-min] = counting_array[i-min] - 1

			
