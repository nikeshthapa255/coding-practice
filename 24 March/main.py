"""

[(1, 1), (2, 0), (4, 2), (5, 3), (6, 4)]

"""

def find_max_min(arr: list[int]) -> int:
    index_arr = [[val, idx] for idx, val in enumerate(arr)]
    index_arr.sort()
    n = len(arr)
    i_min = 0
    i_max = n
    min_sum = 0
    max_sum = 0
    print(index_arr)
    for val, idx in index_arr:
        l, r = 0 if i_min > idx else i_min, n if i_min <= idx else i_min
        min_sum += abs(r - idx) * abs(idx - l + 1) * val
        i_min = max(i_min, idx)
        print(i_min, min_sum, abs(r - idx), abs(idx - l + 1), val)


    for val, idx in index_arr[::-1]:
        l, r = 0 if i_max > idx else i_max, n if i_max <= idx else i_max
        max_sum += abs(r - idx) * abs(idx - l + 1) * val
        i_max = min(i_max, idx)
        print(i_max, max_sum, abs(r - idx), abs(idx - l + 1), val)

    return max_sum - min_sum


print(find_max_min( [2, 1, 4, 5, 6]
))

assert find_max_min([1]) == 0
assert find_max_min([1, 2]) == 1