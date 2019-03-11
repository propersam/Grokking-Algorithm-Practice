
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
        return lowest_cost_node

graph = {}

# setting the graph for node 'start'
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# Setting the graph for node 'a'
graph["a"] = {}
graph["a"]["fin"] = 1
# Setting The graph for node 'b'
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {} # This finish node does not have any neighbours

# Code to make the table containing the costs
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Hash table for the parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = [] # Register to hold already processed nodes
## Done with setup

# Dijktra's algorithm to get shortest distance
node = find_lowest_cost_node(costs) # find the lowest cost node
while node is not None: # If node is not yet processed
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # Go through all the neighbors of this node.
        new_cost = cost + neighbors[n] # If its cheaper to get to this neighbor
        if costs[n] > new_cost:
            costs[n] = new_cost # update the cost for this node
            parents[n] = node # This node becomes new parent for this neighbor
        processed.append(node) # Mark the node as processed
        node = find_lowest_cost_node(costs)
