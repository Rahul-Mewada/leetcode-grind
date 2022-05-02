'''
nums-  1 1 1 2 2 3 3 3     k - 2
                 i
dict- {
    1 : 3
    2 : 2
    3 : 3
}
    
min_h- 3 1
 

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1
        
        min_heap = []
        
        for num in num_freq:
            if len(min_heap) < k:
                heapq.heappush(min_heap, (num_freq[num], num))
            elif min_heap[0][0] < num_freq[num]:
                    heapq.heapreplace(min_heap, (num_freq[num], num))
        
        results = []
        for i in range(k):
            _, num = heapq.heappop(min_heap)
            results.append(num)
        
        return results