big_num = 50000000000000 
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)] 
  
    def minKey(self, key, mst_set): 
        # finding out the minimum value 
        min_i = -1
        min_value = big_num
        for i in range(self.V): 
            if  (mst_set[i] == False) and (key[i] < min_value): 
                min_value = key[i] 
                min_i = i 
        return min_i
  
    def primMST(self): 
        parent = [None] * self.V  
        mst_set = [False] * self.V 
        key = [big_num] * self.V 
        key[0] = 0 
        parent[0] = -1 
        for c in range(self.V): 
            u = self.minKey(key, mst_set) 
            mst_set[u] = True
            for v in range(self.V): 
                if ((self.graph[u][v] > 0) and (key[v] > self.graph[u][v]) and (mst_set[v] == False)): 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
        counter = 0
        for i in range(1, self.V):
            counter += self.graph[i][parent[i]]
        print(counter)

n = int(input())
dots = []
my_set = set()
for i in range(n):
    x_point, y_point = map(int, raw_input().split())
    my_set.add((x_point, y_point))

for item in my_set:
    dots.append(item)
g = Graph(len(my_set))

for i in range(len(my_set)):
    for j in range(len(my_set)):
        g.graph[i][j] = abs(dots[i][0] - dots[j][0]) + abs(dots[i][1] - dots[j][1])
g.primMST()
