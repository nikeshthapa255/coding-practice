
from collections import defaultdict

def find_next_edges(node: list[int], matrix: list[list[int]]):
    row, col = node
    curr_val = matrix[row][col]
    op = [[1, 0], [0, 1], [-1, 0], [0, -1]] 
    return [(row+opr, col+opc) 
        for opr, opc in op
            if 0<= row + opr < len(matrix)  and 0<= col + opc < len(matrix[0]) and matrix[row+opr][col+opc] < curr_val
    ]


def find_depth(start: list[int], matrix: list[list[int]], depth: dict[int]):
    row, col = start
    if depth[(row, col)] != 0: return
    depth[(row, col)] = 1

    next_edges = find_next_edges(start, matrix)

    for r, c in next_edges:
        find_depth((r, c), matrix, depth)
        depth[(row, col)] = max(depth[(row, col)], 1 + depth[(r, c)])


def find_replacement(arr: list[list[int]]) -> list[list[int]]:
    # create adj list
    n, m = len(arr), len(arr[0])
    depth = defaultdict(int)

    # find depth
    for row in range(n):
        for col in range(m):
            find_depth((row, col), arr, depth)
            
    # new value
    new_arr = [[depth[(row, col)] for col in range(m)] for row in range(n)]
    return new_arr


print(find_replacement( [[3,1],[2,5]])) # [[2, 1], [1, 2]]
print(find_replacement( [[10]]))
"""
[1, 2]
[3, 4]

depth = {
    (0,0): 1, 
    (0, 1): 2
    (1, 0): 2,
    (1, 1): 3
}

[1, 2]
[2, 3]
"""