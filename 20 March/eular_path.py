tree = {
    1: [2, 4],
    2: [3],
    4: [5, 6],
}
from collections import defaultdict
from math import log

def dfs(node, tree, first, path, height, current_height = 0):
        path.append(node)
        first[node] = len(path) - 1
        height[node] = current_height
        for next_node in tree.get(node, []):
            dfs(next_node, tree, first, path, height, current_height + 1)
            path.append(node)

def eular_path(tree: dict[int, list[int]]) -> list[int]:
    first = defaultdict(int)
    path = []
    height = defaultdict(int)
    
    dfs(1, tree, first, path, height)
    return [path, first, height]


# Build sparse table
class SparseTable:
    def __init__(self, path, height):
        N = len(path)
        self.N = N
        self.height = height
        self.path = path
        self.lg_count = int(log(N, 2)) + 1
        self.dp = []
        self.build()

    def compare(self, dp, node1, node2):
        value1, value2 = dp[node1[0]][node1[1]], dp[node2[0]][node2[1]]
        h1 = self.height[value1] if value1 != float('inf') else float('inf')
        h2 = self.height[value2] if value2 != float('inf') else float('inf')
        return value1 if h1 < h2 else value2
    
    def build(self):
        dp = [[float('inf')]*self.N for _ in range(self.lg_count)]
        
        dp[0] = self.path[:]

        for idx in range(1, self.lg_count):
            for node_idx in range(self.N):
                if node_idx + (1<<(idx-1)) >= self.N: continue
                dp[idx][node_idx] = self.compare(
                    dp, 
                    [idx-1, node_idx], 
                    [idx-1, node_idx + ( 1<<(idx - 1) )]
                    ) 
        print(dp)
        self.dp = dp

    def query(self, l, r):
        lg_range_length = int(log( r - l + 1, 2))
        print('query', l, r, lg_range_length,  r - (1<<lg_range_length))
        return self.compare(
            self.dp, 
            [lg_range_length, l],
            [lg_range_length, r - (1<<lg_range_length)]
            )

        


def lca(start, end, first, st):
    start_index = first[start]
    end_index = first[end]
    if start_index > end_index:
        start_index, end_index = end_index, start_index
    return st.query(start_index, end_index)


def find_lca(tree: dict[int, list[int]], query: list[list[int]]) -> list[int]:
    path, first, height = eular_path(tree)
    print(path, first, height)
    st = SparseTable(path, height)

    return [lca(start_node, end_node, first, st) for start_node, end_node in query]

        
            
ans = [[1, 2, 1, 3, 1], {1: 0, 2: 1, 3: 3}, {1: 0, 2: 1, 3: 1}]
assert eular_path({1: [2, 3]}) == ans

assert eular_path(tree)[0] == [1, 2, 3, 2, 1, 4, 5, 4, 6, 4, 1]

assert find_lca(tree, [[1, 2], [5, 6], [3, 5]]) == [1, 4, 1]

print(find_lca(tree, [[1, 2], [5, 6], [3, 5]]))