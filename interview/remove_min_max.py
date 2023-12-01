def find_min_deletion(arr):
    mn_idx, mx_idx = 0, 0 # min index and max index
    ln = len(arr) # array length 
    for idx, val in enumerate(arr):
        # update min
        if arr[mn_idx] < val: mn_idx = idx
        # update max
        if arr[mx_idx] > val: mx_idx = idx
    min_max_range = [min(mn_idx, mx_idx), max(mn_idx, mx_idx)] 
    
    """
    mn, mx
    1, 2  = [1, 2]
    4, 1 = [1, 4]
    """
    return ln - (min_max_range[1] - min_max_range[0] + 1)

# TC - O(n)
# SC - O(1)

"""
[]
mn, mx
0, 0
0, 1
2, 1
2, 3
2, 4

4-2+1 = 3
6 - 3 = 3

"""

print(find_min_deletion([2, 3, 1, 6, 8, 4]))