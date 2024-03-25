from bisect import bisect_left as bl,  bisect_right as br

def find_common_free_time_in_schedule(schedule: list[list[list[int, int]]]) -> list[list[int]]:
    overall_occupied_time = []
    for employee_schedule in schedule:
        overall_occupied_time.extend(employee_schedule)
    
    overall_occupied_time.sort()

    occupied_range = []

    for start, end in overall_occupied_time:
        l, r = bl(occupied_range, start), br(occupied_range, end)
        occupied_range[l:r] = [start] * (l%2 == 0) + [end] * (r%2==0)
    
    print(occupied_range)
    
    return [[n1, n2] for n1, n2 in zip(occupied_range[1::2], occupied_range[2::2])] 


print(find_common_free_time_in_schedule( [[[1,2],[5,6]],[[1,3]],[[4,10]]]
))