'''
 [[1,2],[3,5],[7,71]
              [6,7]
          
 [1, 2], [3, 5]
 
Cases
1) newInterval overlaps with one or more and has to be merged
2) newInterval does not overlap and has to be inserted
    - newInterval has to be inserted at the start
    - newInterval has to be inserted at the end
    - newInterval has to be inserted in the middle
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        merge = newInterval
        results = []
        for i, interval in enumerate(intervals):
            if merge:
                if merge[1] < interval[0]:
                    results.append(merge)
                    results.append(interval)
                    merge = None
                    continue
                elif interval[1] >= merge[0]:
                    results.append(merge)
                    self.add(results, interval)
                    merge = None
                    continue
                results.append(interval)
            else:
                self.add(results, interval)
                
        if merge:
            results.append(merge)
        return results
            
            
    def add(self, results, interval):
        if len(results) == 0:
            results.append(interval)
        else:
            last = results[-1]
            if last[0] <= interval[0] <= last[1] or interval[0] <= last[0] <= interval[1]:
                results[-1] = [min(last[0], interval[0]), max(last[1], interval[1])]
            else:
                results.append(interval)
                
                