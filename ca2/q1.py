n, m = [int(x) for x in raw_input().split()]
array = [int(x) for x in raw_input().split()]
sums = [0]
flag = False
for i in xrange(len(array)):
	for j in xrange(len(sums)):
		a = array[i] + sums[j]
		if (a == n):
			print(1)
			flag = True
			break
		if((not(a in sums)) and (a < n)):
			sums.append(a)
	if (flag):
		break
if not(flag):
	print(0)