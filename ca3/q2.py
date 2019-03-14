count = 0
class Node:
	def __init__(self, x_cord, y_cord):
		global count
		self.x = x_cord
		self.y = y_cord
		self.index = count
		count += 1
	def distance(self, a):
		return (abs(self.x - a.x) + abs(self.y - a.y))


n = int(input())
nodes = []
for i in xrange(n):
	x, y  = [int(x) for x in raw_input().split()]
	nodes.append(Node(x, y))
distances = [[-1]*n]*n
for i in xrange(n):
	for j in xrange(i + 1):
		distances[i][j] = nodes[i].distance(nodes[j])
for i in xrange(n):
	for j in xrange(n):
	print(distances[i][j], i, j)