# Group Members:
# Caleb Mabuka: CIT-227-030/2021
# Joram Kariuki: CIT-227-009/2021
# JohnMark Wanjugu: CIT-227-008/2021
# Thorne Musau: CIT-227-029/2021


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
    '0': {'1': 4, '7': 8},
    '1': {'0': 4, '2': 8, '7':11},
    '2': {'1': 8, '3': 7, '5': 4, '8': 2},
    '3': {'2': 7, '4': 9, '5': 14},
    '4': {'3': 9, '5': 10},
    '5': {'2': 4, '3': 14, '4': 10, '6':2},
    '6': {'5': 2, '7': 1, '8': 6},
    '7': {'0': 8, '1': 11, '6': 1, '8': 7},
    '8': {'2': 2, '6': 6, '7': 7}
}

# Specify the start node
start_node = input("Enter the start node: ")

# Run Dijkstra's algorithm
distances, predecessors = dijkstra(graph, start_node)

# Print the results
print("Shortest distances from", start_node, ":")
for node, distance in distances.items():
    print(f"To {node}: {distance}")

print("\nPredecessor nodes:")
for node, predecessor in predecessors.items():
    print(f"{node}: {predecessor}")
