'''
min number of rooms
- if two meetings don't overlap they can use the same room
- if two meetings overlap they need 2 rooms

[0, 15], [5, 10], [15, 20], [17, 30], [32, 40]
                                        i

rooms = [8]
min_room = 2
Worst Case -> n^2
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 1
        
        rooms = []
        intervals.sort(key = lambda x: x[0])
        merged = False
        for interval in intervals:
            start, end = interval[0], interval[1]
            for i, meeting_end_time in enumerate(rooms):
                if start >= meeting_end_time:
                    rooms[i] = end
                    merged = True
                    break
            
            if not merged:
                rooms.append(end)
            
            merged = False
        
        return len(rooms)