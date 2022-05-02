'''
nums-  1 1 1 2 2 3 3 3     k - 2
                 i
dict- {
    1 : 3
    2 : 2
    3 : 3
}
    

'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1
        
        freq_arr = [None] * (len(nums) + 1)
        
        for num in num_freq:
            freq = num_freq[num]
            if freq_arr[freq]:
                freq_arr[freq].append(num)
            else:
                freq_arr[freq] = [num]
        
        print(freq_arr)
        results = []
        
        for i in reversed(range(len(freq_arr))):
            if k == 0:
                return results
            
            if not freq_arr[i]:
                continue
            
            for nums in freq_arr[i]:
                results.append(nums)
                k -= 1
        
        return results