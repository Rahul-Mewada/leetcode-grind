'''
first- [0,2],[5,10],[13,23],[24,25]
second -[1,5],[8,12],[15,24],[25,26]

result = [1,2], [5,5], [8, 10], [15, 23], [24, 24], [25, 25]

[24, 25] [25, 26]


1) If they intersect
    - discard the interval with smaller end?
    - pop new element from left of corresponding list
2) If not
    -?
'''

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        f, s = 0,0
        results = []
        
        while f < len(firstList) and s < len(secondList):
            first = firstList[f]
            second = secondList[s]
            
            overlap = self.intersection(first, second)
            if overlap:
                results.append(overlap)
            
            if first[1] < second[1]:
                f += 1
            else:
                s += 1
        
        return results
        
    def intersection(self, one, two):
        startO, endO = one[0], one[1]
        startT, endT = two[0], two[1]
        intersection = []
        if (startO <= startT <= endO) or (startT <= startO <= endT):
            intersection = [
                max(startO, startT),
                min(endO, endT)
            ]
        return intersection