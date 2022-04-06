'''
[8,11]

first = [8,9]
second =[8,11]

count = 3
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        
        intervals.sort(key = lambda x : -x[0])
        count, f, s = 0, 0, 1
        first = None
        second = intervals.pop()
            
        while intervals:
            first = second
            second = intervals.pop() if intervals else None
            while self.isOverlapping(first, second):
                if first[1] < second[1]:
                    second = intervals.pop() if intervals else None
                else:
                    first = second
                    second = intervals.pop() if intervals else None
                count += 1
                
        return count
                
    def isOverlapping(self, first, second):
        print(first, second)
        if not first or not second:
            return False
        start_first, end_first = first[0], first[1]
        start_sec, end_sec = second[0], second[1]
        if (start_first <= start_sec < end_first) or (start_sec <= start_first < end_sec):
            return True
        
        print(False)
        return False