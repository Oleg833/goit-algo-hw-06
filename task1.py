import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_nodes_from(["Перехрестя 1", "Перехрестя 2", "Перехрестя 3", "Перехрестя 4", "Перехрестя 5", "Перехрестя 6", "Перехрестя 7", "Перехрестя 8", "Перехрестя 9", "Перехрестя 10"])


G.add_edge("Перехрестя 1", "Перехрестя 2", weight=5)
G.add_edge("Перехрестя 1", "Перехрестя 3", weight=3)
G.add_edge("Перехрестя 2", "Перехрестя 3", weight=2)
G.add_edge("Перехрестя 2", "Перехрестя 4", weight=7)
G.add_edge("Перехрестя 3", "Перехрестя 4", weight=4)
G.add_edge("Перехрестя 4", "Перехрестя 5", weight=6)
G.add_edge("Перехрестя 5", "Перехрестя 6", weight=4)
G.add_edge("Перехрестя 4", "Перехрестя 7", weight=3)
G.add_edge("Перехрестя 7", "Перехрестя 8", weight=5)
G.add_edge("Перехрестя 6", "Перехрестя 8", weight=2)
G.add_edge("Перехрестя 7", "Перехрестя 9", weight=4)
G.add_edge("Перехрестя 8", "Перехрестя 9", weight=6)
G.add_edge("Перехрестя 9", "Перехрестя 10", weight=3)

fixed_positions = {"Перехрестя 1": (0, -1), "Перехрестя 2": (1, 2), "Перехрестя 3": (1, -2),
                   "Перехрестя 4": (2, -1), "Перехрестя 5": (3, 2), "Перехрестя 6": (4, -2),
                   "Перехрестя 7": (4, 1), "Перехрестя 8": (5, 2), "Перехрестя 9": (5, -2),
                   "Перехрестя 10": (6, -1)}

plt.figure(figsize=(8, 6))
nx.draw(G, fixed_positions, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, fixed_positions, edge_labels=edge_labels)
plt.title('Граф транспортної мережі міста')
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"\nКількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")

degree_dict = dict(G.degree())
print("\nСтупінь кожної вершини:")
for node, degree in degree_dict.items():
    print(f"{node}: {degree}")
