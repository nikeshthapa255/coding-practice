from collections import deque
import heapq

def dfs(node:int, k:int, adj: list[list[int]], level_count: list[int], indegree: list[int]):
    count = k
    for next_node in adj[node]:
        indegree[next_node] -= 1


# assuming non cyclic
def dfs_depth(node: int, adj: list[list[int]], depth: list[int]):
    if depth[node] != 0: return depth[node]

    depth[node] = 1
    for n_node in adj[node]:
        dfs_depth(n_node, adj, depth)
        depth[node] = max(depth[n_node] + 1, depth[node])

def sorted_depth(arr: list[int], depth: list[int]):
    return deque(sorted(arr, key = lambda x: depth[x]))

def semseter_k_max( n: int, relations: list[list[int]], k: int) -> int:
    depth = [0]*n
    adj = [[] for _ in range(n)]
    indegree = [0]*n
    for s, e in relations:
        adj[s-1].append(e-1)
        indegree[e-1] += 1

    # find deph to each node
    for val in range(n):
        dfs_depth(val, adj, depth)

    print('depth', depth, adj)

    # sort nodes depth wise
    adj = [sorted_depth(val, depth) for val in adj]

    print(adj)

    semester = []

    queue = [[depth[val], val] for val in range(n) if indegree[val] == 0]
    heapq.heapify(queue)
    
    for sem in range(n):
        
        count = 0
        sol = []
        # do topological sort
        while queue and count<k:
            count += 1
            d, element = heapq.heappop(queue)
            sol.append(element)
            for n_node in adj[element]:
                indegree[n_node] -= 1
                if indegree[n_node] == 0:
                    heapq.heappush(queue, [depth[n_node], n_node])


        # add semeseter
        if count:
            semester.append(sol)
    print(semester)
    return len(semester)


print(semseter_k_max(4, [[2,1],[3,1],[1,4]], 2))