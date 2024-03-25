def with_peak(peaks: list[list[int]]) -> int:
    def inside_right_line(point: list[int], peak: list[int]) -> bool:
        x, y = point
        x1, y1 = peak
        return (x + y - (x1 + y1)) <= 0
    
    
    def inside_left_line(point: list[int], peak: list[int]) -> bool:
        x, y = point
        x1, y1 = peak
        return ( x - y - (x1 - y1) ) >= 0 


    valid_peak_count = 0
    for index, peak in enumerate(peaks):
        found = False
        for n_idx, next_peak in  enumerate(peaks):
            if n_idx == index: continue
            print(peak, next_peak, inside_right_line(peak, next_peak), inside_left_line(peak, next_peak))
            if inside_right_line(peak, next_peak) and inside_left_line(peak, next_peak):
                found = True
                break
        if found == False:
            print(peak)
            valid_peak_count += 1
    
    return valid_peak_count


# assert with_peak([[2, 4], [6, 6], [10, 4], [10, 4]]) == 2

# print(with_peak([[1, 3], [2, 2], [3, 1], [4, 4], [5, 3], [6, 2], [7, 5]]))

print(with_peak([[2,2],[6,3],[5,4]]))