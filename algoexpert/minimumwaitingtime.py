def minimum_waiting_time(duration_array):
    duration_array.sort()
    total_waiting_time = 0
    for idx, duration in enumerate(duration_array):
        total_waiting_time += (duration * (len(duration_array)-(idx+1)))
    return total_waiting_time


if __name__ == '__main__':
    array = [3, 2, 1, 2, 6]
    result = minimum_waiting_time(array)
    print(result)
