def sorted_array(m: int, n: int, num1: list[int], num2: list[int]) -> None:
    sol = []
    idx1, idx2 = 0, 0
    while idx1 < m and idx2<n:
        if num1[idx1] < num2[idx2]:
            sol.append(num1[idx1])
            idx1 += 1
        else:
            sol.append(num2[idx2])
            idx2 += 1
    
    while idx1<m:
        sol.append(num1[idx1])
        idx1 += 1
    
    while idx2<n:
        sol.append(num2[idx2])
        idx2 += 1
    
    num1[:] = sol[:]

def sorted_array_without_extra_space(m: int, n: int, num1: list[int], num2: list[int]) -> None:
    num1[:] = [0]
    

num1 = [1, 3, 4, 0, 0]
num2 = [2, 5]
sorted_array(3, 2, num1, num2)
assert num1 == [1, 2, 3, 4, 5], 'Correct update Test Case 1'

nums1 = [0] 
m = 0
nums2 = [1]
n = 1
sorted_array(m, n, nums1, nums2)
print(nums1)