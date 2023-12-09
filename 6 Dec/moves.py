def solve(nums: list[int]) -> int: # min difference max-min values
    # if len(nums) <= 4: return 0
    # sort the array
    arr = sorted(nums)
    ans = arr[-1] - arr[0] 
    arr = [arr[0]]*3 + arr + [arr[-1]]*3
    def reccursive_sol(l, r, moves = 3):
        nonlocal ans
        if l==r:
            ans = 0
            return
        while l<r and moves:
            l_diff = arr[l+1] - arr[l]
            r_diff = arr[r] - arr[r-1]
            # print('s1', l, r, arr[l:r+1])
            if l_diff>r_diff:
                l += 1
            elif l_diff < r_diff:
                r -= 1
            else:
                reccursive_sol(l+1, r, moves-1)
                reccursive_sol(l, r-1, moves-1)
                break
            moves -= 1
            ans = min(ans, abs(arr[r] - arr[l]))
            # print('ans', ans, l, r)
    reccursive_sol(3, len(arr)-4)

    return ans


print(solve( [5,3,2,4]))

"""
 [1,5,0,10,14]
"""