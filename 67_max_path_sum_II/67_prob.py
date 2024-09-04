import re


# Create identifier for each of the 100 rows
rows = [row for row in range(0,100)]
# Create empty edge list
edge_list = {}

for index, row in enumerate(rows):
    # Skip first character "A"
    if index == 0:
        pass
    else:
        # Deal with first edge case on far right of row
        Fnode = str(row) + "-" + str(index)
        Tnode = str(row-1) + "-" + str(index-1)
        edge_list[Fnode] = Tnode
        index -= 1
        # Whist row position is greater than 0
        while index > 0:
            # Add node to nodes list
            Fnode = str(row) + "-" + str(index)
            Tnode = [(str(row-1) + "-" + str(index)), (str(row-1) + "-" + str(index-1))]
            edge_list[Fnode] = Tnode
            # Remove one from required nodes
            index -= 1
        # Final edge case on far left, when index position = 0
        Fnode = str(row) + "-" + str(index)
        Tnode = str(row-1) + "-" + str(index)
        edge_list[Fnode] = Tnode

# Add the first row, not included in edge-list
nodes = ["0-0"]
# Add all the other nodes in the triangle
for key in edge_list.keys():
    nodes.append(key)


# Sort the nodes in ascending order, left to right
nodes = sorted(nodes, key=lambda x: (int(x.split('-')[0]), int(x.split('-')[1])))
# Initialise two variables
node_weight = {}
values = []

# Open the triangle text file with the values
with open("0067_triangle.txt", "r") as file:
    for line in file:
        # Extract each number
        for item in re.findall(r"(\d{2})", line):
            # Append to values list (as an int)
            values.append(int(item))

# For each node
for index, node in enumerate(nodes):
    # Assign it its respective value, and store it in node_weight dictionary
    node_weight[node] = values[index]

# For each Fnode in the edge_list
for node in edge_list.keys():
    # Collect the connections for this node
    connections = edge_list[node]
    # If it is a list (contains 2 values)
    if isinstance(connections, list):
        # Find the max value attributable to each of these connections
        max_value = max(node_weight[conn] for conn in connections)
    else:
        # Otherwise, the max value must be the one its connected to
        max_value = node_weight[connections]
    # Update the node_weight of the path resepctively
    node_weight[node] += max_value

# Collect the maximum path weights from the bottom row at the end
bottom_row = [node for node in nodes if node.startswith('99')]
# And find the maximum possible weight of any path through the triangle
max_path_sum = max(node_weight[node] for node in bottom_row)
# Print it
print("The maximum path sum is:", max_path_sum)