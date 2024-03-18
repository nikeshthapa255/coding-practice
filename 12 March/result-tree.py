"""
Input: root = [3,5,4,2,null,1,1,1,0], result = true

observaton
i -> 2*i + 2, 2*i + 1
"""

op_map = {
    2: [
        [[0, 0]],
        [[1, 1], [1, 0], [0, 1]]
    ],
    3: [
        [[0, 0], [1, 0], [0, 1]],
        [[1, 1]]
    ],
    4: [
        [[0, 0], [1, 1]],
        [[1, 0], [0, 1]]
    ],
    5: [
        [[1]],
        [[0]]
    ]
}

max_int = float('inf')
def find_solution(root: list[int], root_result: bool) -> int:
    arr_length = len(root)
    dp = [[max_int, max_int] for _ in range(arr_length*2)] #[0] -> min op to get zero, [1] -> min operation for one
    
    """
    a0, b0 = op_map[root[i]][0]
    a1, b1 = op_map[root[i]][1]
    dp[i][0] = min(dp[2*i+1][a0]+dp[2*i+2][b0], ..rest )
    dp[i][1] = min(dp[2*i+1][a1]+dp[2*i+2][b1], ..rest )
    """

    for idx in range(arr_length-1, -1, -1):
        value = root[idx]

        # null node
        if value == None: continue
        
        # leaf node
        if value == 0:
            dp[idx] = [0, 1]
        elif value == 1:
            dp[idx] = [1, 0]
        elif value == 5: # NOT operation
            c1, c2 = 2*idx + 2, 2*idx + 1
            # c1 is always a valid solution
            if c2<arr_length and root[c2] != None:
                c1 = c2
            dp[idx][0] = min(
                dp[idx][0],
                dp[c1][1]
            )
            dp[idx][1] = min(
                dp[idx][1],
                dp[c1][0]
            )
        else: # 2, 3, 4
            c1, c2 = 2*idx + 2, 2*idx + 1
            for op in range(2):
                options =  op_map[value][op]
                dp[idx][op] = min([dp[idx][op]] + [dp[c1][o1] + dp[c2][o2] for o1, o2 in options])
    # print(dp)
    return dp[0][1 if root_result == True else 0]


# print('ans',find_solution([3,5,4,2,None,1,1,1,0], True))

print('ans',find_solution([0], False))
