n, m = [int(x) for x in raw_input().split()]
array = [[int(x), 0] for x in raw_input().split()]
temp = [int(x) for x in raw_input().split()]
for i in xrange(n):
	array[i][1] = temp[i]
rooms = []
for i in xrange(m):
	rooms.append([0, 0])
sorted_list = sorted(array, key=lambda x: x[0])
flag = True
for i in xrange(n):
	for j in xrange(m):
		if (sorted_list[i][0] >= rooms[j][1]):
			rooms[j][0] = sorted_list[i][0]
			rooms[j][1] = sorted_list[i][1]
			break
		elif (j == m - 1):
			print(0)
			flag = False
	if not(flag):
		break
if (flag):
	print(1)