import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    while stack:
        current_vertex, path = stack.pop()

        if current_vertex == goal:
            return path

        visited.add(current_vertex)

        for edge in graph.edges(current_vertex):
            neighbor = edge[1]
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return []


def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_vertex, path = queue.popleft()

        if current_vertex == goal:
            return path

        visited.add(current_vertex)

        for edge in graph.edges(current_vertex):
            neighbor = edge[1]
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []


G = nx.DiGraph()

G.add_nodes_from(["B 1", "B 2", "B 3", "B 4", "B 5", "B 6", "B 7", "B 8", "B 9", "B 10"])

edges = [("B 1", "B 2", {"weight": 5}), ("B 1", "B 3", {"weight": 3}),
         ("B 2", "B 3", {"weight": 2}), ("B 2", "B 4", {"weight": 7}),
         ("B 3", "B 4", {"weight": 4}), ("B 4", "B 5", {"weight": 6}),
         ("B 5", "B 6", {"weight": 4}), ("B 4", "B 7", {"weight": 3}),
         ("B 7", "B 8", {"weight": 5}), ("B 6", "B 8", {"weight": 2}),
         ("B 7", "B 9", {"weight": 4}), ("B 8", "B 9", {"weight": 6}),
         ("B 9", "B 10", {"weight": 3})]

G.add_edges_from(edges)

fixed_positions = {"B 1": (0, -1), "B 2": (1, 2), "B 3": (1, -2),
                   "B 4": (2, -1), "B 5": (3, 2), "B 6": (4, -2),
                   "B 7": (4, 1), "B 8": (5, 2), "B 9": (5, -2),
                   "B 10": (6, -1)}

start_node = "B 1"
goal_node = "B 10"

print("\nШлях за допомогою DFS:")
print(dfs(G, start_node, goal_node))

print("\nШлях за допомогою BFS:")
print(bfs(G, start_node, goal_node))


plt.figure(figsize=(8, 6))
nx.draw(G, fixed_positions, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, arrowsize=20)
edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}
nx.draw_networkx_edge_labels(G, fixed_positions, edge_labels=edge_labels)
plt.title('Направлений граф транспортної мережі міста')
plt.show()