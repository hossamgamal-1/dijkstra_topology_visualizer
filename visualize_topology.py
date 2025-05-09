import networkx as nx
import matplotlib.pyplot as plt

def visualize_topology(graph: nx.DiGraph) -> None:
    """Visualizes the network topology using matplotlib."""
    pos: Dict[str, Any] = nx.spring_layout(graph)
    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(graph, pos, node_size=500, node_color='lightblue')
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), 
                          edge_color='gray', arrowstyle='->', arrowsize=20)
    nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
    edge_labels: Dict[Tuple[str, str], float] = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10)
    plt.title("Network Topology Visualization")
    plt.axis('off')
    plt.show()
