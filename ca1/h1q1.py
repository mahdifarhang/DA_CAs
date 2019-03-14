file = open("input.txt", 'r')
a = (int(x) for x in file.read().split(' '))
array = list(a)
print(min(array))


def func(arr, first, last):
	if (last-first == 0):
		return [-10000, arr(first), arr(first)]
	# elif(last-first == 1):
	# 	return [arr(last)-arr(first), min(arr), max(arr)]
	print(first, last)
	list(r1)=func(arr, first, (last-first)/2)
	list(r2)=func(arr, (last-first)/2+1,last)
	return [max(r1[0],r2[0],r2[2]-r1[1]), min(r1[1], r2[1]), max(r1[2], r2[2])]

list(m)=func(array, 0, len(array)-1)
print(m[0])

