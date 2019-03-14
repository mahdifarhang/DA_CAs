def calculate_max_sum_with_and_without_one_element(array):
	if (len(array) == 0):
		return 0, 0;
	maxwith, maxwithout = calculate_max_sum_with_and_without_one_element(array[0:-1])
	return maxwithout + array[-1], max(maxwith, maxwithout)
n = int(input())
arr = [int(x) for x in raw_input().split()]
print(max(calculate_max_sum_with_and_without_one_element(arr)))