from typing import List

class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        # Validate inputs
        if not all(isinstance(i, int) for i in A + B):
            raise ValueError("Both arrays should contain only integers.")

        na, nb = len(A), len(B)
        n = na + nb
        
        if n == 0:  # Check for empty input arrays
            raise ValueError("Both arrays cannot be empty.")

        def solve(k, a_start, a_end, b_start, b_end):
            if a_start > a_end: 
                return B[k - a_start]
            if b_start > b_end: 
                return A[k - b_start]

            a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
            a_value, b_value = A[a_index], B[b_index]

            if a_index + b_index < k:
                if a_value > b_value:
                    return solve(k, a_start, a_end, b_index + 1, b_end)
                else:
                    return solve(k, a_index + 1, a_end, b_start, b_end)
            else:
                if a_value > b_value:
                    return solve(k, a_start, a_index - 1, b_start, b_end)
                else:
                    return solve(k, a_start, a_end, b_start, b_index - 1)
        
        if n % 2:
            return solve(n // 2, 0, na - 1, 0, nb - 1)
        else:
            return (solve(n // 2 - 1, 0, na - 1, 0, nb - 1) + solve(n // 2, 0, na - 1, 0, nb - 1)) / 2


# Test cases
solution = Solution()

# Basic tests
assert solution.findMedianSortedArrays([1, 3], [2]) == 2.0, "Test case 1 failed"
assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5, "Test case 2 failed"
assert solution.findMedianSortedArrays([], [1]) == 1.0, "Test case 3 failed"
assert solution.findMedianSortedArrays([2], []) == 2.0, "Test case 4 failed"
assert solution.findMedianSortedArrays([1, 3], [2, 7, 10]) == 3.0, "Test case 5 failed"

# Edge cases
assert solution.findMedianSortedArrays([1], [1]) == 1.0, "Test case 6 failed"
assert solution.findMedianSortedArrays([1, 1, 1, 1], [1, 1, 1, 1, 1]) == 1.0, "Test case 7 failed"
assert solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7, 8]) == 4.5, "Test case 8 failed"

print("All tests passed!")
