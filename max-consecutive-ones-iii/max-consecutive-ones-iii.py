'''
[1] k = 3
 lr
   
 
 
 Sliding Window Approach
 1) Start with left and right pointers at zero
 2) If nums[right] == 1:
        right ++ 
    elif k > 0:
        k--
        right++
    elif k <= 0:
        
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, longest_length = 0,0,0
        if nums[left] == 0:
            k -= 1
            if k >= 0:
                longest_length += 1
            
        while right < len(nums):
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
                if left > right:
                    right = left
                    if right < len(nums) and nums[right] == 0:
                        k -= 1
            else:
                right += 1
                if right < len(nums) and nums[right] == 0:
                    k -= 1              
                
            if k >= 0 and right < len(nums) and left < len(nums):      
                length = (right - left) + 1
                longest_length = max(longest_length, length)
            
        return longest_length