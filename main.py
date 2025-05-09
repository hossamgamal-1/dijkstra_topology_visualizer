from visualize_topology import visualize_topology
from create_graph import create_graph
from compute_forwarding_tables import compute_forwarding_tables

def main():
    nodes = ['u', 'v', 'w', 'x', 'y', 'z']

    edges = [   
        ('u', 'v', 2),
        ('u', 'w', 5),
        ('u', 'x', 1),
        ('x', 'v', 2),
        ('v', 'w', 3),
        ('x', 'w', 3),
        ('w', 'y', 1),
        ('x', 'y', 1),
        ('w', 'z', 5),
        ('y', 'z', 2),
    ]
    
    # Create network graph
    G = create_graph(nodes, edges)
    
    # Compute forwarding tables
    forwarding_tables = compute_forwarding_tables(G)
    
    # Print forwarding tables
    for node in sorted(forwarding_tables.keys()):
        print(f"Forwarding table for node {node}:")
        for dest in sorted(forwarding_tables[node].keys()):
            print(f"  {dest} -> {forwarding_tables[node][dest]}")
    
    # Visualize topology
    visualize_topology(G)

if __name__ == "__main__":
    main()