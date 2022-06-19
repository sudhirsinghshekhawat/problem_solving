from typing import List

import pytest


def no_of_platform(arrivals: List[int], departures: List[int]) -> int:
    arrivals.sort()
    departures.sort()

    n = len(arrivals)
    i = 1
    j = 0
    count = 1

    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1

    return count


@pytest.mark.parametrize("arrivals,departures,output", [([100, 200, 300, 400], [200, 300, 400, 500], 2)])
def test_no_of_platform(arrivals, departures, output):
    assert output == no_of_platform(arrivals, departures)
