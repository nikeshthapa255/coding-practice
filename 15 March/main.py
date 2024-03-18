from collections import defaultdict, deque

def max_color_frequency(n, edges, colors):
    # Initialize adjacency list, indegree array, and count array
    adj = defaultdict(list)
    indegree = [0] * n
    count = [[0 for _ in range(26)] for _ in range(n)]  # 26 for each letter in the alphabet
    answer = 0
    
    # Build the graph and indegree array
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    
    # Initialize queue with all nodes having indegree 0
    q = deque([i for i in range(n) if indegree[i] == 0])
    
    # Number of nodes seen in topological order
    nodes_seen = 0
    
    # BFS traversal to perform topological sort
    while q:
        node = q.popleft()
        nodes_seen += 1
        # Increment the frequency of the color of node and update answer
        color_index = ord(colors[node]) - ord('a')  # Convert color char to index
        count[node][color_index] += 1
        answer = max(answer, count[node][color_index])
        
        # For each neighbor, update frequencies and decrement indegree
        for neighbor in adj[node]:
            for i in range(26):  # Update all color frequencies
                count[neighbor][i] = max(count[neighbor][i], count[node][i])
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    
    # Check for a cycle
    if nodes_seen < n:
        return -1  # Cycle detected
    
    return answer

# Example usage
edges = [[0,1],[1,2],[2,3],[0,3],[3,4],[4,5],[5,6],[6,7],[4,7],[7,8],[6,9],[7,9],[8,9],[5,9],[8,10],[7,10],[10,11],[9,11],[8,11],[11,12],[5,12],[11,13],[12,13],[13,14],[12,14],[8,14],[10,14],[14,15],[13,15],[12,15],[15,16],[12,16],[8,16],[16,17],[15,18],[18,19],[17,19],[19,20],[12,20],[17,20],[20,21],[18,21],[19,22],[21,22],[22,23],[21,23],[22,24],[23,25],[24,25],[22,25],[25,26],[26,27],[20,27],[25,28],[13,28],[26,28],[25,29],[27,30],[30,31],[13,31],[28,31],[31,32],[26,32],[21,32],[27,32],[30,33],[32,33],[31,33],[26,33],[31,34],[25,34],[23,34],[5,35],[32,35],[30,36],[20,36],[29,36],[35,36],[35,37],[34,37],[36,37],[32,37],[27,38],[19,39],[28,39],[5,39],[38,40],[39,40],[22,41],[35,41],[38,41],[40,41],[24,42],[40,42],[30,43],[40,43],[41,43],[39,44],[22,45],[41,45],[33,45],[43,45],[42,46],[43,46],[44,46],[44,47],[30,47],[43,48],[47,48],[48,49],[48,50],[49,50],[45,51],[34,51],[37,51],[45,52],[49,53],[36,53],[52,54],[46,54],[53,55],[52,56],[55,56],[51,57],[56,57],[50,57],[53,58],[35,58],[43,59],[47,59],[54,59],[45,60],[57,60],[47,60],[58,61],[35,61],[61,62],[52,63],[48,63],[47,63],[56,64],[61,64],[52,64]]  # Directed edges
colors = "qqxfhffrqxqbhhrfrsfxbfxhxxhsfbhbfqqfrsqsqhbrmhmsqxrhfxhffssmrfxhr"  # Colors of each node
n = len(colors) # Number of nodes

print(max_color_frequency(n, edges, colors))  # Output will be the maximum frequency of any color
