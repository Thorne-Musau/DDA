import heapq

# Dijkstra algorithm function
def dijkstra(graph, start):
    # Initialize distances and predecessor dictionary
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    
    # Priority queue to keep track of nodes with their distances
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Check if the current path is shorter than the stored distance
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path is found, update distance and predecessor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, predecessors

# Example usage:

# Define a graph as an adjacency dictionary
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Specify the start node
start_node = input(print("Enter the start node: "))

# Run Dijkstra's algorithm
distances, predecessors = dijkstra(graph, start_node)

# Print the results
print("Shortest distances from", start_node, ":")
for node, distance in distances.items():
    print(f"To {node}: {distance}")

print("\nPredecessor nodes:")
for node, predecessor in predecessors.items():
    print(f"{node}: {predecessor}")
