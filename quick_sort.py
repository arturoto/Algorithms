

def quick_sort(nums, low, high):


	if low >= high:
		return

	pivot = partition(nums, low, high)
	quick_sort(array, low, pivot-1)
	quick_sort(array, pivot+1, high)



 

def partition(nums, low, high):


	pivot_index = (low + high)//2

	swap(nums, pivot_index, high)


	i = low

	for j in range(low, high, 1):

		if nums[j] <= nums[high]:

			swap(nums, i, j)
			i += 1

	swap(nums, i, high)

	return i



def swap(nums, i , j):

	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp
