import networkx as nx
import matplotlib.pyplot as plt

# https://networkx.github.io/documentation/stable/reference/classes/graph.html#networkx.Graph

G=nx.Graph()

# G = nx.petersen_graph()
# G = nx.tutte_graph()
# G = nx.sedgewick_maze_graph()
# G = nx.tetrahedral_graph()
G.add_node(1)
G.add_nodes_from([2, 3, 4, 5])
# G.add_nodes_from(range(100, 110))
# H = nx.path_graph(10)
# G.add_nodes_from(H)
# G.add_node(H)
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (4, 5)])
# # print("Nodes of graph: ")
# # print(G.nodes())
# # print("Edges of graph: ")
# # print(G.edges())
# plt.subplot(121)

nx.draw(G, with_labels=True, font_weight='bold')
# plt.subplot(122)

# nx.draw(G, nlist=[1], with_labels=True, font_weight='bold')
plt.show()