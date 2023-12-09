from typing import List




def create_new_tree(idx: int, base_tree: List[int]) -> List[int]:
    # return tree
    ln = len(base_tree)
    new_tree = [idx]
    
    # bfs to look for nodes
    stack = new_tree[:]
    deleted_set = set()
    while stack:
        n_stack = []
        for idx in stack:
            if idx//2 in deleted_set: deleted_set.add(idx)
            if base_tree[idx] == None: deleted_set.add(idx)
            l, r = idx*2, idx*2+1
            if l<ln :   
                n_stack.append(l)
            if r<ln : n_stack.append(r)
        new_tree.extend(n_stack)
        stack = n_stack
    # convert idx to value1
    sol = [base_tree[idx] if idx not in deleted_set else None  for idx in new_tree]
    while sol[-1] == None:
        sol.pop()
    return sol


def solve(tree: List[int], to_delete: List[int]) -> List[int]:
    # if length of tree is zero
    if len(tree) == 0:
        return []
    
    curr_tree = [-1] + tree
    roots_list = [curr_tree[1]]
    ln = len(curr_tree) # length of the tree
    # value to index dict
    idx_dict = { value: idx for idx, value in enumerate(curr_tree)}
    for delete_value in to_delete:
        value_idx = idx_dict[delete_value]
        next_roots =[curr_tree[root] for root in  [value_idx*2, value_idx*2+1] if root<ln]
        roots_list.extend(next_roots)
        curr_tree[value_idx] = None
    
    # remove deleted nodes
    deleted_set = set(to_delete)
    return [create_new_tree(root, curr_tree) for root in roots_list if root not in deleted_set]

assert solve([1, 2, 3, 4, 5, 6, 7], [3, 5]) == [[1, 2, None, 4], [6], [7]]

print(solve([1,2,4,None,3], [3]))
