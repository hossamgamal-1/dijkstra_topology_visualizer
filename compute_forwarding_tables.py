import networkx as nx
from typing import *
import heapq

def compute_forwarding_tables(graph: nx.DiGraph) -> Dict[str, Dict[str, str]]:
    """Computes forwarding tables for all nodes using Dijkstra's algorithm."""
    adj_list = get_adjacency_list(graph)
    forwarding_tables: Dict[str, Dict[str, str]] = {}
    for node in graph.nodes():
        distances, predecessors = dijkstra(adj_list, node)
        forwarding_table: Dict[str, str] = {}
        for dest in graph.nodes():
            if dest != node:
                next_hop = get_next_hop(node, dest, predecessors)
                if next_hop:
                    forwarding_table[dest] = next_hop
        forwarding_tables[node] = forwarding_table
    return forwarding_tables

def get_adjacency_list(graph: nx.DiGraph) -> Dict[str, Dict[str, float]]:
    """Extracts the adjacency list from the given graph."""
    adj_list: Dict[str, Dict[str, float]] = {}
    for node in graph.nodes():
        adj_list[node] = {}
        for neighbor in graph.neighbors(node):
            adj_list[node][neighbor] = graph[node][neighbor]['weight']
    return adj_list

def dijkstra(adj_list: Dict[str, Dict[str, float]], start: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
    """Implements Dijkstra's algorithm to find the shortest paths from the start node."""
    distances: Dict[str, float] = {node: float('infinity') for node in adj_list}
    predecessors: Dict[str, Optional[str]] = {node: None for node in adj_list}
    distances[start] = 0.0
    priority_queue: List[Tuple[float, str]] = [(0.0, start)]
    visited: Set[str] = set()
    
    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for neighbor, weight in adj_list[current_node].items():
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_dist, neighbor))
    
    return distances, predecessors

def get_next_hop(start: str, dest: str, predecessors: Dict[str, Optional[str]]) -> Optional[str]:
    """Determines the next hop node from start to dest using predecessors."""
    if predecessors[dest] is None:
        return None
    current: Optional[str] = dest
    path: List[str] = []
    while current != start and current is not None:
        path.append(current)
        current = predecessors[current]
    if current != start:
        return None  # No path exists
    path.append(start)
    path.reverse()
    return path[1] if len(path) >= 2 else None
