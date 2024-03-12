def min_op(arr: list[int]) -> int:
    
    ln = len(arr)
    sol = float('inf')
    def find_displacement(arr, patt = 0):
        sol = list(range(1, ln))
        if patt:
            sol = [0] + sol
        else:
            sol = sol + [0]
        return sum(+(a!=b) for a, b in zip(sol, arr))

    def op(arr, zero_pos, pattern = 0, recur = 0):
        if recur>10: return 0
        # print('s1', arr)
        ans = []
        curr_disp = find_displacement(arr)
        if curr_disp == 0: 
            return 0
        for idx, val in enumerate(arr):
            if (idx + pattern)%ln != val:
                # do some operation
                arr[idx], arr[zero_pos] = arr[zero_pos], arr[idx]
                if (find_displacement(arr) < curr_disp):
                    ans.append(1 + op(arr, idx, pattern, recur + 1))
                arr[idx], arr[zero_pos] = arr[zero_pos], arr[idx]

        if (curr_disp != 0 and not ans):
            idx = (zero_pos + 1)%ln
            arr[idx], arr[zero_pos] = arr[zero_pos], arr[idx]
            ans.append(1 + op(arr, idx, pattern, recur + 1))
            arr[idx], arr[zero_pos] = arr[zero_pos], arr[idx]
        # print(arr, ans)
        if ans:
            return min(ans)
        return 0
    zero_pos = arr.index(0)
    return min(op(arr, zero_pos, 0), op(arr, zero_pos, 1))
        
# print('sol', min_op(list(map(int, input().split()))))
print('sol', min_op([1,2,3,4,0]))