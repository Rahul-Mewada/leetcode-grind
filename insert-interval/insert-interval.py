'''
1) Start with a temp pair
2) iterate thru the pairs array
3) if temp pair and current pair intersect: -> temp_pair = [min(lower,lower), max(upper, upper)]


[[3, 5]] , [1,2]


'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
    
        temp_pair = newInterval
        lower_temp, upper_temp = newInterval[0], newInterval[1]
        merged = []
        temp_merged = False
        
        for index, pair in enumerate(intervals):
            lower_curr, upper_curr = pair[0], pair[1]
            lower_temp, upper_temp = temp_pair[0], temp_pair[1]
            
            if self.doIntersect(pair, temp_pair):
                temp_pair = [min(lower_curr, lower_temp), max(upper_curr, upper_temp)]
            else:
                if temp_pair[1] < lower_curr:
                    merged.append(temp_pair)
                    merged += intervals[index:len(intervals)]
                    temp_merged = True
                    break
                else:
                    merged.append(pair)
            
        if not temp_merged:
            merged.append(temp_pair)
            
        return merged
            
    def doIntersect(self, pair, target):
        lower_pair, upper_pair = pair[0], pair[1]
        lower_target, upper_target = target[0], target[1]
        
        if lower_pair <= lower_target <= upper_pair:
            return True
        elif (lower_target <= lower_pair) and (upper_target >= lower_pair):
            return True
        else:
            return False
        