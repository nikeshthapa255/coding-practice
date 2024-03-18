def generate_pascal(N = 10):
    ans = [[1], [1, 1]]
    for _ in range(N-2):
        new_row = [1] + [ans[-1][idx] + ans[-1][idx+1] for idx in range(len(ans[-1]) - 1)] + [1]
        ans.append(new_row)
    return ans

print(*generate_pascal(10), sep='\n')
        