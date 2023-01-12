graph = {
    "A": {"B": 6, "C": 2, "D": float("inf")},           # Draw a graph -> Directed Acyclic Graph
    "B": {"D": 1},                                      # ----------------------------------------
    "C": {"B": 3, "D": 5},                              # Directed Acyclic Graph is the only graph
    "D": {}                                             # with which Dijkstra's algorithm works
}


def find_lowest_cost_node(start):                       # Find the lowest cost of node
    lowest_cost = float("inf")                          # Default cost of node with lowest cost is infinity
    lowest_cost_node = None                             # Default node with lowest cost is None
    for node in graph[start]:                           # Go through all nodes
        if start == node:                               # Chech if current node is not the start
            continue
        cost = graph[start][node]                       # Get a cost of current node
        if cost < lowest_cost:                          # If cost of current node is lower than previous cost then:
            lowest_cost = cost                          # - Change the cost of node with lowest cost
            lowest_cost_node = node                     # - Change the node with lowest cost
    return lowest_cost_node


def dijkstra(start, end):
    node = find_lowest_cost_node(start)                 # Find a node with lowest cost
    new_cost = graph[start][node]                       # Get a cost of node
    if node != end:                                     # Check if current node is not the end
        while node is not None:                         # While nodes is exists loop is working
            cost = graph[start][node]                   # Get a cost of node for calculations
            neighbors = graph[node]                     # Get the neighbors of node
            for neighbor in neighbors.keys():           # Go through neighbors of current node
                new_cost = cost + neighbors[neighbor]   # Calculate potential new cost
                if graph[start][neighbor] > new_cost:   # If you can get faster to neighbor through the current node then:
                    graph[start][neighbor] = new_cost   # - Update a cost of node
            del graph[start][node]                      # Delete node because it is processed
            node = find_lowest_cost_node(start)         # Find new node
    return new_cost


print(dijkstra("A", "D"))
