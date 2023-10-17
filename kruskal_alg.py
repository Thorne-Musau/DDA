# Group Members:
# Caleb Mabuka: CIT-227-030/2021
# Joram Kariuki: CIT-227-009/2021
# JohnMark Wanjugu: CIT-227-008/2021
# Thorne Musau: CIT-227-029/2021


class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.label_to_index = {}

    def addEdge(self, u, v, w): 
        # Map node labels to integers
        if u not in self.label_to_index:
            self.label_to_index[u] = len(self.label_to_index)
        if v not in self.label_to_index:
            self.label_to_index[v] = len(self.label_to_index)
        
        self.graph.append([self.label_to_index[u], self.label_to_index[v], w]) 

    def find(self, parent, i): 
        if parent[i] != i: 
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 

    def union(self, parent, rank, x, y): 
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 
        else: 
            parent[y] = x 
            rank[x] += 1

    def KruskalMST(self): 
        result = [] 
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2]) 
        parent = [] 
        rank = [] 

        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 

        while e < self.V - 1: 
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 

            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 

        minimumCost = 0
        print("Edges in the constructed MST") 
        for u, v, weight in result: 
            # Print the original node labels
            u_label = next(key for key, value in self.label_to_index.items() if value == u)
            v_label = next(key for key, value in self.label_to_index.items() if value == v)
            minimumCost += weight 
            print(f"{u_label} -- {v_label} == {weight}") 
        print("Minimum Spanning Tree", minimumCost) 

# Driver code 
if __name__ == '__main__': 
    g = Graph(6)
    g.addEdge("A", "B", 3)
    g.addEdge("A", "C", 1)
    g.addEdge("A", "D", 4)
    g.addEdge("C", "F", 3)
    g.addEdge("F", "E", 2)
    g.addEdge("B", "E", 3)
    
    g.KruskalMST() 