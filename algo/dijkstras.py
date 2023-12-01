import heapq
from typing import Dict

class PriorityQueue:
    # adj = {'key': value}
    def __init__(self, adj: Dict[str, int] = {}):
        self.value_version = {}
        self.heap = []
        for key, value in adj.items():
            self.add(key, value)

    def add(self, key, value):
        self.value_version[key] = self.value_version.get(key, 0) + 1
        heapq.heappush(self.heap, [value, self.value_version[key], key])
    
    # remove the smallest
    def remove(self):
        # remove the smallest value with correct version
        while self.heap:
            value, version, key = heapq.heappop(self.heap)
            if version > 10: break
            if self.value_version.get(key, 0) > version: 
                continue
            return [key, value]
        return None
    def __str__(self):
        return f'{self.heap}\n {self.value_version}'

pq = PriorityQueue({
    'a': 1, 'b': 3
})
pq.add('a', 2)
assert pq.remove() == ['a', 2]


"""
Used to find weighted shortest path from the sources to all nodes.
"""
def dijkstra(adj: dict, source: str):
    # find all pair shorted path
    
    # initialize inifite nodes
    inf = float('inf')
    wt = {key: inf for key in adj.keys()}
    wt[source] = 0
    visited = set()
    heap = PriorityQueue(wt)
    while 1:
        last_value = heap.remove()
        if last_value == None: break

        key, min_wt = last_value
        if key in visited: continue
        visited.add(key)
        wt[key] = min_wt
        for node, node_wt in adj[key].items():
            if node in visited: pass
            heap.add(node, min_wt + node_wt)
    return wt





# example
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'), dijkstra(graph, 'B'), dijkstra(graph, 'C'), dijkstra(graph, 'D'), sep='\n')