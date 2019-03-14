n = int(input())
arr = [int(x) for x in raw_input().split()]
result = 0
backup = [(arr[x]) for x in xrange(len(arr))]
arr.sort()
for i in xrange(len(arr)):
	if(arr[-1] in backup):
		if(backup.index(arr[-1]) == 0):
			del backup[0:2]
		elif(backup.index(arr[-1]) == len(backup)-1):
			del backup[-2:]
		else:
			# if (backup[backup.index(arr[-1])] > backup[backup.index(arr[-1])+1]+backup[backup.index(arr[-1])-1]): the problem begins here
			del backup[backup.index(arr[-1])-1:backup.index(arr[-1])+2]
			# else:
				# result -= arr[-1]
				# backup[backup.index(arr[-1])]=0
		result += arr[-1]
	del arr[-1]
print result