import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import heapq

stations={0: 'Aluva',1: 'Pulinchodu', 2: 'Companypady', 3: 'Ambattukavu', 4: 'Muttom', 5: 'Kalamassery', 6: 'Cochin University',7: 'Pathadipalam',8: 'Edapally',9: 'Changampuzha Park',10: 'Palarivattom',11: 'JLN Stadium',12: 'Kaloor', 13: 'Town Hall', 14: 'M.G Road',15: 'Maharajas College', 16: 'Ernakulam South', 17: 'Kadavanthra', 18: 'Elamkulam', 19: 'Vyttila',20:'Thaikoodam'}

def draw_graph(data):
  G = nx.Graph()
  for source, dest in data.keys():
      weight = data[(source,dest)]
      G.add_edge(stations[source], stations[dest], weight=weight)
  pos = nx.kamada_kawai_layout(G)
  labels = nx.get_edge_attributes(G, 'weight')
  nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightblue', font_size=10, font_weight='bold')
  nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
  plt.show()

edges = {(0, 1): 5.47,(1, 2): 3.78,(2, 3): 3.25,(3, 4): 2.72,(4, 5): 2.19,(5, 6):3.1,(6, 7): 1.7,(7, 8): 1.5,(8,9):1.5,(9,10):1.7,(10,11):2.2,(11,12):1.1,(12,13):1.0,(13,14):0.9,(14,15):0.8,(15,16):0.7,(16,17):1.3,(17,18):1.2,(18,19):1.1,(19,20):1.0,(0,19):1.0}



draw_graph(edges)

import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    paths = {node: [] for node in graph}
    visited = set()

    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [current_node]
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, paths

graph = {0: [(1, 5.47), (19, 1.0)],
         1: [(2, 3.78), (0, 5.47)],
         2: [(3, 3.25), (1, 3.78)],
         3: [(4, 2.72), (2, 3.25)],
         4: [(5, 2.19), (3, 2.72)],
         5: [(6, 3.1), (4, 2.19)],
         6: [(7, 1.7), (5, 3.1)],
         7: [(8, 1.5), (6, 1.7)],
         8: [(9, 1.5), (7, 1.5)],
         9: [(10, 1.7), (8, 1.5)],
         10: [(11, 2.2), (9, 1.7)],
         11: [(12, 1.1), (10, 2.2)],
         12: [(13, 1.0), (11, 1.1)],
         13: [(14, 0.9), (12, 1.0)],
         14: [(15, 0.8), (13, 0.9)],
         15: [(16, 0.7), (14, 0.8)],
         16: [(17, 1.3), (15, 0.7)],
         17: [(18, 1.2), (16, 1.3)],
         18: [(19, 1.1), (17, 1.2)],
         19: [(0, 1.0), (18, 1.1)]}


source_node = 1
shortest_distances, shortest_paths = dijkstra(graph, source_node)

print("Shortest distances from node {}:".format(source_node))
for node, distance in shortest_distances.items():
    print("\n")
    print("Node {}: Distance = {}".format(node, distance))
    if node != source_node:
        path = shortest_paths[node] + [node]
        print("Path: {}".format(" -> ".join(map(str, path))))


graph=shortest_paths
edges2=[]
for node, neighbors in graph.items():
  if len(neighbors)>0:
    edges2=edges2+[[node,neighbors[len(neighbors)-1]]]


edges2

from networkx import exception
G = nx.Graph()
for node in graph:
    G.add_node(stations[node])
for node, neighbor in edges2:
  try:
    G.add_edge(stations[node], stations[neighbor],weight=edges[(node,neighbor)])
  except:
    G.add_edge(stations[node], stations[neighbor],weight=edges[(neighbor,node)])
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightblue', font_size=8, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
plt.title("Dijkstra's Shortest Path")
plt.axis('off')
plt.show()