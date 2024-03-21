def bfs(start: int, adj: int, height: list[int], visited: set[int, int]) -> int: 
    if start in visited:
        return height[start]

    visited.add(start)
    height[start] = 1
    curr_height = 1
    height[start] = max(height[start], curr_height)
    stack = [start]
    curr_visited = set({start})
    while stack:
        next_stack = []
        curr_height += 1
        for node in stack:
            for next_node in adj[node]:
                if next_node in curr_visited:
                    # cycle case
                    return -1
                visited.add(next_node)
                curr_visited.add(next_node)
                next_stack.append(next_node)
                height[next_node] = max(height[next_node], curr_height)
        stack = next_stack

"""
height = [1, 2, 3, 0]
next_stack = [1]

stack = [2]
next_stack = []
return -1 
"""           



def find_min_semester(course_count: int, relations: list[list[int]]) -> int:
    # create adjacency list 
    adj = [[] for _ in range(course_count)]

    for start, end in relations:
        adj[start-1].append(end-1)

    # bfs
    visited = set()
    height = [0]*course_count

    for val in range(course_count):
        result = bfs(val, adj, height, visited)
        if result == -1:
            return -1 # cycle case

    return max(height)



assert find_min_semester(3, [[1, 2], [1, 3]]) == 2

assert find_min_semester(4, [[1, 2], [2, 3], [3, 1]]) == -1

"""
adj = [[1, ], [2, ], [0], []]
visited = {}
height = [0, 0, 0, 0]

bfs(0

Input: n = 3, relations = [[1,3],[2,3]]
Input: n = 3, relations = [[1,2],[2,3],[3,1]]
"""

print(find_min_semester(3, [[1,3],[2,3]]))

print('-------------------')

print(find_min_semester(3, [[1,2],[2,3],[3,1]]))