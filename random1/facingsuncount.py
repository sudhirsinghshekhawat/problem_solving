def facing_sun_count(array):
    current_height = array[0]
    building_count = 1
    for i in range(1, len(array)):
        if array[i] > current_height:
            building_count += 1
            current_height = array[i]
    return building_count


if __name__ == '__main__':
    array = [7, 4, 8, 2, 9]
    result = facing_sun_count(array)
    print(result)

    array = [2, 3, 4, 5]
    result = facing_sun_count(array)
    print(result)
