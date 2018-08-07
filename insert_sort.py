

'''
start in from, if less shift.
consider every number preceding the compare dnumber.
Flash memory. insertion good
'''


def insertion_sort(nums):


	for i in range(len(nums)):

		j = i

		while j > 0 and nums[j-1] > nums[j]:

			swap(nums, j, j-1)

			j -= 1

	return nums



def swap(nums, i , j):

	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp
