n = int(input())
arr = [int(x) for x in raw_input().split()]
max_with = max_without = 0
for i in xrange(len(arr)):
	a = max_with
	max_with = max_without + arr[i]
	max_without = max(max_without, a)
print(max(max_with, max_without))