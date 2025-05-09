import networkx as nx
from typing import *

def create_graph(nodes: List[str], edges: List[Tuple[str, str, float]]) -> nx.DiGraph:
    """Creates and returns a directed graph from given edges."""
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    for src, dest, weight in edges:
        G.add_edge(src, dest, weight=float(weight))
    return G