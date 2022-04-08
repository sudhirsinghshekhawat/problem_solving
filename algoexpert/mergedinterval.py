# time complexity = O(nlogn) Space complexity : O(n)
def merge_overlap_interval(interval_array):
    sorted_intervals = sorted(interval_array, key=lambda x: x[0])
    current_interval = sorted_intervals[0]
    merged_intervals = [current_interval]

    for next_interval in sorted_intervals:
        _, current_interval_end = current_interval
        next_interval_start, next_interval_end = next_interval

        if current_interval_end >= next_interval_start:
            current_interval[1] = max(current_interval_end, next_interval_end)
        else:
            current_interval = next_interval
            merged_intervals.append(current_interval)
    return merged_intervals


if __name__ == '__main__':
    interval_array = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
    result = merge_overlap_interval(interval_array)
    print(result)
