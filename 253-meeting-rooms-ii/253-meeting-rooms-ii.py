import heapq
'''
min number of rooms
- if two meetings don't overlap they can use the same room
- if two meetings overlap they need 2 rooms

[4, 9], [2, 15], [16, 23], [9, 29], [36, 45]
                             i

[0, 30], [5, 10], [15, 20]
            i

30

'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        soonest_ending = None
        intervals.sort(key= lambda x : x[0])
        rooms = []
        
        for interval in intervals:
            if not rooms:
                heapq.heappush(rooms, interval[1])
            else:
                earliest_meeting = rooms[0]
                if interval[0] >= earliest_meeting:
                    heapq.heapreplace(rooms, interval[1])
                else:
                    heapq.heappush(rooms, interval[1])
            
        return len(rooms)
        
    

            