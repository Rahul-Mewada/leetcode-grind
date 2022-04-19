'''
Sliding Window?

 0 0 1 1 0 0 1
             s 
               e

1 : 1


count = 5
 
 min(num of 1's, num of 0's)
'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        bs = BinarySubstrings(s)
        return bs.count_bin_substrings()
    
class BinarySubstrings:
    def __init__(self, bin_string):
        self.nums = bin_string
    
    def count_bin_substrings(self):
        if len(self.nums) == 1:
            return 0
        
        count, start, end = 0,0,0
        nums = self.nums
        num_freq = {}
        
        while end < len(nums):
            if nums[end] in num_freq:
                num_freq[nums[end]] += 1
            else:
                num_freq[nums[end]] = 1
                
            while len(num_freq) == 2 and (end == len(nums)-1 or nums[end] != nums[end+1]):
                count += min(num_freq['0'], num_freq['1'])
                start_freq = num_freq[nums[start]]
                num_freq.pop(nums[start])
                start += start_freq
            
            end += 1
            
        return count
                
        