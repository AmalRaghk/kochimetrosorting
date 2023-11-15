import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from collections import defaultdict, deque
edges =[['Aluva', 'Pulinchodu'],
  ['Pulinchodu', 'Companypady'],
  ['Companypady', 'Ambattukavu'],
  ['Ambattukavu', 'Muttom'],
  ['Muttom', 'Kalamassery'],
  ['Kalamassery', 'Cochin University'],
  ['Cochin University', 'Pathadipalam'],
  ['Pathadipalam', 'Edapally'],
  ['Edapally', 'Changampuzha Park'],
  ['Changampuzha Park', 'Palarivattom'],
  ['Palarivattom', 'JLN Stadium'],
  ['JLN Stadium', 'Kaloor'],
  ['Kaloor', 'Town Hall'],
  ['Town Hall', 'M.G Road'],
  ['M.G Road', 'Maharajas College'],
  ['Maharajas College', 'Ernakulam South'],
  ['Ernakulam South', 'Kadavanthra'],
  ['Kadavanthra', 'Elamkulam'],
  ['Elamkulam', 'Vyttila'],
  ['Aluva','Vyttila'],
  ['Cochin University','Aluva']
]

def draw_graph(data):
  G = nx.Graph()
  for row in data:
      source, dest = row
      G.add_edge(source, dest)
  pos = nx.kamada_kawai_layout(G)
  nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightblue', font_size=5, font_weight='bold')
  plt.show()

draw_graph(edges)

graph = defaultdict(list)
for edge in edges:
    source, dest = edge
    graph[source].append(dest)
    graph[dest].append(source)

def bfs(graph, start):
    ticket={'Aluva': 23, 'Pulinchodu': 42, 'Companypady': 31, 'Ambattukavu': 78, 'Muttom': 56, 'Kalamassery': 90, 'Cochin University': 67, 'Pathadipalam': 12, 'Edapally': 83, 'Changampuzha Park': 45, 'Palarivattom': 27, 'JLN Stadium': 61, 'Kaloor': 5, 'Town Hall': 34, 'M.G Road': 19, 'Maharajas College': 72, 'Ernakulam South': 96, 'Kadavanthra': 80, 'Elamkulam': 63, 'Vyttila': 48}
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print("Station is "+ str(node)+" , ticket collected="+str(ticket[node]))  # Process the node (you can change this part)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

start_node = 'Aluva'
print("BFS traversal starting from station", start_node, ":")
bfs(graph, start_node)
