'''
 [1, 4] [2, 3]
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        cur_interval = None
        merged_intervals = []
        for i, interval in enumerate(intervals):
            if not cur_interval:
                cur_interval = interval
                continue
            
            cur_start, cur_end = cur_interval[0], cur_interval[1]
            start, end = interval[0], interval[1]
            
            if cur_start <= start <= cur_end:
                cur_interval = [cur_start, max(end, cur_end)]
            else:
                merged_intervals.append(cur_interval)
                cur_interval = interval
                
        merged_intervals.append(cur_interval)
        
        return merged_intervals