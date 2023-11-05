def solve(N, A):
    two_count_factors = 0
    simple_arr = []
    for val in A:
        val_copy = val
        while val_copy%2 == 0:
            two_count_factors += 1
            val_copy //= 2
        simple_arr.append(val_copy)
    
    # generate new array
    for index in range(1, N):
        prev_val = simple_arr[index-1]
        current_val = simple_arr[index]
        while two_count_factors and prev_val >= current_val:
            current_val *= 2
            two_count_factors -= 1
        if current_val <= prev_val:
            return 'NO'
        simple_arr[index] = current_val
    
    return 'YES'


    """
    We have an array A, 
    a1, a2, a3, ... aN
    operation 
    - pick i, j and i != j
    - A[i] % 2 == 0
    - do this ai //= 2, aj *= 2
    """
    """
    Observations 
    - if no even number than we cannot do any operation
    - 


    ex - [a1, a2] a1>a2
    [8, 3] - 4, 6 -> 
    1000, 11
    ex - 2: 4, 2, 5, 10, 2
    1, 10, 101, 1010, 1000 
    4 -> 2

    ex 3 - [3, 2, 4]
    11, 100, 1
    
    ex 4 - [2, 6, 3]
    1, 11, 1100
    """

    """
    Solution
    - extract all 2's 
    - start multiplying incrementally
    """

print(solve(3, [2, 6, 3]))
print(solve(1, [2]))
print(solve(3, [3, 2, 4]))