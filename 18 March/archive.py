def push_pop(push_array: list[int], pop_array: list[int]) -> bool:
    pop_pointer = 0
    pop_length = len(pop_array)
    new_push = []
    for value in push_array:
        new_push.append(value)
        while pop_pointer<pop_length and pop_array[pop_pointer] == new_push[-1]:
            pop_pointer += 1
            new_push.pop()
    return pop_pointer == pop_length and len(new_push) == 0

assert push_pop([1, 2, 3], [3, 2, 1]) == True

assert push_pop([1, 3, 5], [2, 3, 1]) == False

assert push_pop([2], [2]) == True

# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
print(push_pop([1,2,3,4,5], [4,3,5,1,2]))
