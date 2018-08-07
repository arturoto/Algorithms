

def selection_sort(nums):

	for i in range(len(nums) - 1):

		index = i

		for j in range(i + 1, len(nums), 1):

			if nums[j] < nums[index]:

		if index != i:

			swap(nums, index, i)
	return nums


def swap(nums, i , j):

	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp
