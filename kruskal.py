import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
def draw_graph(data):
  G = nx.Graph()
  for row in data:
      source, dest, weight = row
      G.add_edge(source, dest, weight=weight)
  pos = nx.spring_layout(G)
  labels = nx.get_edge_attributes(G, 'weight')
  nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightblue', font_size=10, font_weight='bold')
  nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
  plt.show()
l=[[0, 1, 1760],
 [1, 2, 970],
 [2, 3, 990],
 [3, 4, 940]]

draw_graph(l)
l=[[0, 1, 1760],
 [1, 2, 970],
 [2, 3, 990],
 [3, 4, 940],
 [5, 1, 890],
 [5, 3, 989],
 [6, 4, 784],
 [6, 0, 456]]
draw_graph(l)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if 0 <= x < len(self.parent) and self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

def kruskal(edges):

    edges.sort(key=lambda x: x[2])

    num_nodes = len(set([edge[0] for edge in edges] + [edge[1] for edge in edges]))
    min_spanning_tree = []
    union_find = UnionFind(num_nodes)

    for edge in edges:
        source, dest, weight = edge
        if union_find.find(source) != union_find.find(dest):
            min_spanning_tree.append((source, dest, weight))
            union_find.union(source, dest)

    return min_spanning_tree


edges = [[0, 1, 1760],
 [1, 2, 970],
 [2, 3, 990],
 [3, 4, 940],
 [5, 1, 890],
 [5, 3, 989],
 [6, 4, 784],
 [6, 0, 456]]


minimum_spanning_tree = kruskal(edges)
mst=[]

for edge in minimum_spanning_tree:
  mst.append([edge[0],edge[1],edge[2]])
draw_graph(mst)

