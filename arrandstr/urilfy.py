def urlify(string: str):
    space_counter = 0
    for char in string:
        if char == ' ':
            space_counter = space_counter + 1
    size_of_array = len(string) + (2 * space_counter)
    char_array = [None] * size_of_array
    length = size_of_array - 1

    for i, char in reversed(list(enumerate(string))):
        if char == ' ':
            char_array[length] = '0' # type:ignore
            char_array[length - 1] = '2'  # type:ignore
            char_array[length - 2] = '%'  # type:ignore
            length = length - 3
        else:
            char_array[length] = char  # type:ignore
            length = length - 1

    print(''.join(char_array))   # type:ignore


urlify('sudhir singh')
urlify('sudhir singh shekhawat')
