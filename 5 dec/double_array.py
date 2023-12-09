from typing import List, Dict

def get_counter(array: List[int]) -> Dict[int, int]:
    count = {}
    for value in array:
        count[value] = count.get(value, 0) + 1
    return count

def solve(changed_array: List[int]) -> List[int]:
    # count each value 
    counter = get_counter(changed_array)
    ans = []
    
    # check if valid array
    for key, value in counter.items():
        # odd count check
        if value%2: return [] # invalid array 
        ans.extend([key]*(value//2))

    # return the original array in any order
    
    return ans


assert get_counter([1, 1]) == {1: 2}
assert solve([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
print(solve([6,3,0,1]))