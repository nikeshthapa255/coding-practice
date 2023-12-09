def solve(arr: list[int]) -> int:
    count = 0
    ans = 0
    for value in arr:
        if value == 1:
            count += 1
        else: count = 0
        ans = max(count, ans)
    return ans


assert solve([1, 0, 1, 1]) == 2
assert solve([1]) == 1
assert solve([]) == 0
assert solve([0]) == 0

print(solve([1,0,1,1,0,1]))