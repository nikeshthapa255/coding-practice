from typing import List
def solve(matrix: List[List[int]]) -> int:
    # create adjecency list
    adj = {} # node: List[nodes]
    row_length, col_length = len(matrix), len(matrix[0])
    
    def check_valid_edge(row, col, prev_value):
        return 0<=row<row_length and 0<=col<col_length and matrix[row][col] > prev_value
            
    def create_edge(row, col, next_row, next_col):
        value = matrix[row][col]
        if check_valid_edge(next_row, next_col, value):
            if (row, col) not in adj: adj[(row, col)] = []
            adj[(row, col)].append((next_row, next_col))

    for row in range(row_length):
        for col in range(col_length):
            value = matrix[row][col]
            for n_col in range(col_length):
                if n_col == col: continue
                create_edge(row, col, row, n_col )
            for n_row in range(row_length):
                if n_row == row: continue
                create_edge(row, col, n_row, col )

    print('adj list', adj)
    
    visited = {}
    stack = []
    def dfs(node):
        print('dfs', node, visited.get(node), stack, adj.get(node, []))
        if node in visited: return visited[node]
        max_height = 1
        sorted_edges = sorted(adj.get(node, []), key=lambda n: -matrix[n[0]][n[1]])
        for next_node in adj.get(node, []):
            # if next_node in stack: continue
            stack.append(next_node)
            max_height = max(max_height, 1 + dfs(next_node))
            stack.pop()
            
        visited[node] = max_height
        return max_height
    
    
    for row in range(row_length):
        for col in range(col_length):
            stack=  [(row, col)]
            dfs((row, col)) 
    
    print('visited', visited)
    
    max_path = max([1] + list(visited.values()))
    return max_path


print('solution \t', solve([[3,1,6],[-9,5,7]]))
    
"""
[3,1,6]
[-9,5,7]
1,5,7
6,7
-9,5,7
-9, 3
5, 7
"""