class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distance = self.eucDistance(point)
            tup = (distance, point)
            heapq.heappush(distances, tup)
            
        results = []
        while k > 0:
            _, point = heapq.heappop(distances)
            results.append(point)
            k -= 1
            
        return results
        
    def eucDistance(self, p1):
        p2 = [0, 0]
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        
        distance = math.sqrt(
            ((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2))
        )
        
        return distance


    