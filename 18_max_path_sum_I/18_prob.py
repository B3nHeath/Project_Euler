import string

# This program is going to find the maximum path sum down a triangle
# We are going to create by creating an edge list of the nodes down the triangle
# letters will indicate rows
# Numbers will indicate position along row

# Create our list of characters
chars = [char for char in string.ascii_uppercase[0:15]]

# Empty list to store all our positions in the triangle
edge_list = {}

# for row number and letter in character list
for row, letter in enumerate(chars):
    # Skip first character "A"
    if row == 0:
        pass
    else:
        # Deal with first edge case on far right of row
        Fnode = letter + str(row)
        Tnode = chr(ord(letter) - 1) + str(row-1)
        edge_list[Fnode] = Tnode
        row -=1
        # If there are still nodes to add
        while row > 0:
            # Add node to nodes list
            Fnode = letter + str(row)
            Tnode = [(chr(ord(letter)-1) + str(row)), (chr(ord(letter)-1) + str(row-1)) ]
            edge_list[Fnode] = Tnode
            # Remove one from required nodes
            row -= 1
        # Final edge case on far left, when index position = 0
        Fnode = letter + str(row)
        Tnode = chr(ord(letter) - 1) + str(row)
        edge_list[Fnode] = Tnode

nodes = ["A0"]
for key in edge_list.keys():
    nodes.append(key)

Values = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

nodes = sorted(nodes, key=lambda x: (x[0], int(x[1:])))
node_weight = {}

for index, node in enumerate(nodes):
    node_weight[node] = Values[index]

for node in edge_list.keys():
    connections = edge_list[node]
    if isinstance(connections, list):
        max_value = max(node_weight[conn] for conn in connections)
    else:
        max_value = node_weight[connections]
    node_weight[node] += max_value


bottom_row = [node for node in nodes if node.startswith('O')]
max_path_sum = max(node_weight[node] for node in bottom_row)

print("The maximum path sum is:", max_path_sum)