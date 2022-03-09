"""
sliding window problem
- keep expanding the window when you come across a one
- keep track of the number of zeros
- while num_zeros > 1 shrink the window
- keep track of max_length
    - return max_length - 1
    
 0 1 1 1 0 1 1 0 1
           s     f

zeros = 1
max_len = 6
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        slow = 0
        num_zeros = 0
        max_len = 0
        
        for fast in range(len(nums)):
            if nums[fast] == 0:
                num_zeros += 1
            while num_zeros > 1:
                if nums[slow] == 0:
                    num_zeros -= 1
                slow += 1
            max_len = max(max_len, fast - slow + 1)
            
        return max_len - 1