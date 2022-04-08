import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda k: k[0])
        available_rooms = []

        heapq.heappush(available_rooms, intervals[0][1])

        for interval in intervals[1:]:
            if available_rooms[0] <= interval[0]:
                heapq.heappop(available_rooms)
            heapq.heappush(available_rooms, interval[1])
        return len(available_rooms)

    def min_meeting_rooms(self, intervals: List[List[int]]):
        if not intervals:
            return 0

        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])

        used_rooms = 0

        L = len(intervals)

        start_pointer = 0
        end_pointer = 0

        while start_pointer < L:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1

            used_rooms += 1
            start_pointer += 1
        return used_rooms


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    s = Solution()
    print(f"result : {s.minMeetingRooms(intervals)}")

    result = s.min_meeting_rooms(intervals)
    print(f"required meeting_rooms = {result}")
