l = int(input())
lengths = [int(x) for x in raw_input().split()]
p = int(input())
points = []
for i in xrange(p):
	points.append(int(input()))
arr = [0]
for i in xrange(len(lengths)):
	for j in xrange(lengths[i]):
		arr.append(i+1)
for i in xrange(p):
	print(arr[points[i]])