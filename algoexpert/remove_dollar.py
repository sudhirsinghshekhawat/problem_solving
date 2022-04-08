def remove_dollar(dictionary):
    result = {}
    for key, value in dictionary.items():
        new_key = key
        if '$' in key:
            new_key = key.replace('$', '_')
        if type(value) == dict:
            result[new_key] = remove_dollar(dictionary[key])
        else:
            result[new_key] = value

    return result


if __name__ == '__main__':
    dictionary = {
        'key1': 'test',
        'key$2': ["test1", "test2"],
        'key$3': {
            'key$34': '1111',
            'key$35': {
                'key$765': 1,
                'key_766': {
                    'key$786': 'value786'
                }
            }
        }
    }
    result = remove_dollar(dictionary)
    print(result)
