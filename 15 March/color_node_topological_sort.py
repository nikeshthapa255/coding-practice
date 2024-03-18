class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        from collections import deque
        node_count = len(colors)
        # create adj
        adj = [[] for _ in range(node_count)]
        node_colors = [[0]* 26 for _ in range(node_count)]
        incomming = [0] * node_count

        # populate adjacency list
        for start_node, next_node in edges:
            adj[start_node].append(next_node)
            incomming[next_node] += 1

        
        ## topological sort using bfs
        # find non incomming nodes
        leaf_nodes = deque([node for node in range(node_count) if incomming[node] == 0])
        
        seen_nodes = 0
        
        while leaf_nodes:
            curr_node = leaf_nodes.popleft()

            # update current node values
            color_index = ord(colors[curr_node]) - ord('a')
            node_colors[curr_node][color_index] += 1
            seen_nodes += 1

            # check neighbours
            for next_node in adj[curr_node]:
                # update it's colors
                for color_index in range(26):
                    node_colors[next_node][color_index] = max(node_colors[next_node][color_index], node_colors[curr_node][color_index])
                
                incomming[next_node] -= 1

                if incomming[next_node] == 0:
                    leaf_nodes.append(next_node)
        
        if seen_nodes < node_count:
            return -1
        
        # response with solution
        return max(max(color_count) for color_count in node_colors)
                

"""

Alright, imagine we're talking about a really big, colorful maze with rooms and one-way doors between them. Each room is painted a different color. We want to find out which color appears the most times on the paths through this maze.

Here's how we solve this like detectives:

Preparing Our Tools (Setting Up the Problem):

Imagine we have a big map of the maze with all the rooms (nodes) and doors (edges) drawn on it.
Each room is painted a certain color. We keep track of this in a special coloring book.
Sorting the Rooms (Kahn's Algorithm):

We need to walk through the maze in a special order so we don't miss anything or walk in circles. This is like lining up all the rooms so we can visit them one by one, making sure we only enter a room after we've visited all rooms with doors leading to it.
We start with rooms that don't have any doors leading to them (these have no "incoming edges").
Every time we walk out of a room, we erase all doors from that room to others in our map. If a room ends up with no doors leading to it, we add it to our list to visit next.
Detecting a Loop (Cycle Detection):

If we follow our special order but find some rooms we never get to visit (because they still have doors leading to them), it means we've found a loop in our maze. That's like being stuck in a loop-de-loop slide at the playground. If this happens, we can't solve the puzzle, so we say "-1".
Counting the Colors (Finding Maximum Frequency):

In each room, we count the color and write it down in our coloring book, keeping track of how many times we've seen each color so far on our path through the maze.
If a room has multiple doors leading to it, we look at the coloring books from each of those rooms and update our counts based on the highest numbers we find. Then, we add one more count for the color of the current room.
We also have a special counter to keep track of the most times we've seen any color in all the paths we've checked.
Walking Through the Maze (Implementing the Algorithm):

We start at the rooms without incoming doors, updating our color counts and the most seen color as we go.
We keep moving through the maze, room by room, following our special order, updating color counts from the paths leading to each room.
If we can visit all rooms without finding a loop, we know the highest count of the most frequent color in our coloring book.
Think of it like a treasure hunt where we're counting colored gems, but we have to follow a specific route through the cave. Our goal is to find out which color gem is the most common on any path through the cave, but we have to make sure we explore the cave in such a way that we don't miss any paths and don't walk in circles.
"""