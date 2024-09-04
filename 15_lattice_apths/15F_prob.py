import networkx as nx
import string
import matplotlib.pyplot as plt

"""
Goal of this program is to find out the number of potential routes to go from top-left of 20x20 grid, to bottom-right of grid. Can only move either right or down. We are shown that for a 2x2 grid, there are 6 potential paths

Solution:
    Create a directed network, with 21 columns and 21 rows to represent each point in the grid. Name columns alphabetically, and rows numerically. Then create edges between each node, and its counterpart 1 across alphabetically, and 1 down numerically. Then calculate the shortest paths (since all routes are same length), and generate a counter for the number of potential paths


    This worked hypothetically, but it took too long. Somewhere around O(n^2) in the maximum case. See the couple of solutions provided in 15_prob.py
"""

ROWS = 21



# initialize an empty graph
g=nx.DiGraph()

# Create an empty list for characters
chars = []

# Append list of characters of desired length
for char in string.ascii_uppercase[0:21]:
    chars.append(char)


"""
This deals with numerical links
"""
# For each character in list
for c in chars:
    # go to each row (-end one)
    for r in range(1,ROWS):
        # Create a from node = combination of character and number e.g. "A1"
        Fnode = c + str(r)
        # Create the node it goes to numerically e.g. "A2"
        Tnode = c + str(r+1)
        # Add edge to network
        g.add_edge(Fnode, Tnode)

"""
This deals with alphabetical links
"""
# For each row
for r in range(1,ROWS+1):
    # Go to each character (-end one)
    for c in chars[:-1]:
        # Create from node
        Fnode = c + str(r)
        # Create to node, 1 across alphabetically e.g. A1 -> B1
        Tnode = chr(ord(c) + 1) + str(r)
        # Add edge to network
        g.add_edge(Fnode, Tnode)



start_node = chars[0] + "1"
end_node = chars[-6] + str(ROWS-5)

print(f"{start_node} -> {end_node}")

count = 0
for path in nx.all_shortest_paths(g, start_node, end_node):
    count+=1

print(count)

# # create an object of all the shortest paths between start and end node
# list = nx.all_shortest_paths(g,start_node, end_node)
# # Create a count variable
# count = 0
# # For each available path, add 1 to the list
# for item in list:
#     count +=1

# print(count)




