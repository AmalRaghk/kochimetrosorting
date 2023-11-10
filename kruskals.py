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

l=[['Aluva', 'Pulinchodu', 5.47],
  ['Pulinchodu', 'Companypady', 3.78],
  ['Companypady', 'Ambattukavu', 3.25],
  ['Ambattukavu', 'Muttom', 2.72],
  ['Muttom', 'Kalamassery', 2.19],
  ['Kalamassery', 'Cochin University', 3.1],
  ['Cochin University', 'Pathadipalam', 1.7],
  ['Pathadipalam', 'Edapally', 1.5],
  ['Edapally', 'Changampuzha Park', 1.5],
  ['Changampuzha Park', 'Palarivattom', 1.7],
  ['Palarivattom', 'JLN Stadium', 2.2],
  ['JLN Stadium', 'Kaloor', 1.1],
  ['Kaloor', 'Town Hall', 1.0],
  ['Town Hall', 'M.G Road', 0.9],
  ['M.G Road', 'Maharajas College', 0.8],
  ['Maharajas College', 'Ernakulam South', 0.7],
  ['Ernakulam South', 'Kadavanthra', 1.3],
  ['Kadavanthra', 'Elamkulam', 1.2],
  ['Elamkulam', 'Vyttila', 1.1]
]


draw_graph(l)
l=[ ['Aluva', 'Pulinchodu', 5.47],
  ['Pulinchodu', 'Companypady', 3.78],
  ['Companypady', 'Ambattukavu', 3.25],
  ['Ambattukavu', 'Muttom', 2.72],
  ['Muttom', 'Kalamassery', 2.19],
  ['Kalamassery', 'Cochin University', 3.1],
  ['Cochin University', 'Pathadipalam', 1.7],
  ['Pathadipalam', 'Edapally', 1.5],
  ['Edapally', 'Changampuzha Park', 1.5],
  ['Changampuzha Park', 'Palarivattom', 1.7],
  ['Palarivattom', 'JLN Stadium', 2.2],
  ['JLN Stadium', 'Kaloor', 1.1],
  ['Kaloor', 'Town Hall', 1.0],
  ['Town Hall', 'M.G Road', 0.9],
  ['M.G Road', 'Maharajas College', 0.8],
  ['Maharajas College', 'Ernakulam South', 0.7],
  ['Ernakulam South', 'Kadavanthra', 1.3],
  ['Kadavanthra', 'Elamkulam', 1.2],
  ['Elamkulam', 'Vyttila', 1.1],
     ["Changampuzha Park", "Kinfra", 4.0],
  ["Changampuzha Park", "Chembumukku", 4.0],
  ["Changampuzha Park", "Padamugal", 4.5],
  ["Kinfra", "Chembumukku", 1.0],
 ["Chembumukku", "Padamugal", 1.5],
 ["Padamugal", "Kakkanad Jn", 2.0],
    ["Aluva", "Pulinchodu", 5.47],
    ["Pulinchodu", "Companypady", 3.78],
    ["Companypady", "Ambattukavu", 3.25],
    ["Ambattukavu", "Muttom", 2.72],
    ["Muttom", "Kalamassery", 2.19],
    ["Kalamassery", "Cochin University", 3.1],
    ["Cochin University", "Pathadipalam", 1.7],
    ["Pathadipalam", "Edapally", 1.5],
    ["Edapally", "Changampuzha Park", 1.5],
    ["Changampuzha Park", "Palarivattom", 1.7],
    ["Palarivattom", "JLN Stadium", 2.2],
    ["JLN Stadium", "Kaloor", 1.1],
    ["Kaloor", "Town Hall", 1.0],
    ["Town Hall", "M.G Road", 0.9],
    ["M.G Road", "Maharajas College", 0.8],
    ["Maharajas College", "Ernakulam South", 0.7],
    ["Ernakulam South", "Kadavanthra", 1.3],
    ["Kadavanthra", "Elamkulam", 1.2],
    ["Elamkulam", "Vyttila", 1.1],
    ["Changampuzha Park", "Kinfra", 4.0],
    ["Changampuzha Park", "Chembumukku", 4.0],
    ["Changampuzha Park", "Padamugal", 4.5],
    ["Kinfra", "Chembumukku", 1.0],
    ["Chembumukku", "Padamugal", 1.5],
    ["Padamugal", "Kakkanad Jn", 2.0]
]

draw_graph(l)

class UnionFind:
    def __init__(self):
        self.parent = {}  # Initialize an empty dictionary

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x  # Initialize the parent for a new vertex
        elif self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
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
    union_find = UnionFind()

    for edge in edges:
        source, dest, weight = edge
        if union_find.find(source) != union_find.find(dest):
            min_spanning_tree.append((source, dest, weight))
            union_find.union(source, dest)

    return min_spanning_tree

minimum_spanning_tree = kruskal(l)
mst = []

for edge in minimum_spanning_tree:
    mst.append([edge[0], edge[1], edge[2]])

draw_graph(mst)