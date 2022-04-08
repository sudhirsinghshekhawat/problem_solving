"""
queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
output = [-1, 2, -1, 2]

"""
from typing import List

queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]


def queries_func(queries: List[int]) -> List[int]:
    query_data = set()
    result_array = []
    for query in queries:
        set_val, get_val = query
        query_data.add(set_val)
        if get_val in query_data:
            result_array.append(get_val)
        else:
            result_array.append(-1)
    return result_array


if __name__ == '__main__':
    result = queries_func(queries)
    print(result)
