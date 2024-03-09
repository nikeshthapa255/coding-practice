# -1 = error, [] - no sol, [....] - sol
def find_sq(arr: list[int], mex: int):
    sq = []
    curr_mex, curr_mex_set = 0, set() 
    for idx, val in enumerate(arr):
        curr_mex_set.add(val)
        while curr_mex in curr_mex_set:
            curr_mex += 1
        if curr_mex > mex:
            return -1
        # print('inter', curr_mex, curr_mex_set, val, idx)
        
        if curr_mex == mex:
            # reset
            sq.append(idx)
            curr_mex, curr_mex_set = 0, set() 
            continue
    return sq
        
def find_mex_sq(n: int, arr: list[int]):
    l, r = 0, n-1
    while l <= r:
        md = (l+r+1)//2
        # check solution found
        sol = find_sq(arr, md)
        print(sol, md, l, r)
        if sol == -1:
            # error l = md
            l = md
        elif sol == []:
            # nothing r = md - 1
            r = md - 1
        else:
            # sol found
            return sol
    return -1

def main():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        arr = list(map(int, input().split()))
        ans = find_mex_sq(n, arr)
        if ans == -1 or len(ans) == 1:
            print(-1)
            continue
        ans = [0] + ans 
        ans = [(a+1, b+1) for a, b in zip(ans, ans[1:])]
        print(*ans, sep='\n')
main()

"""
1
8
0 1 7 1 0 1 0 3
"""