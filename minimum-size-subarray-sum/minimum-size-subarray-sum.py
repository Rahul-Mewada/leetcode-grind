'''
Seems like a sliding window problem 
O(N) time 
O(1) space 

cur = 32

[32,3,7,2,4,3]
    l r
   
 1) Current sum > prev sum: left += 1
 2) Current sum < prev sum: right += 1
 3) Current sum == target: update min length
'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0,0
        cur_sum = nums[0]
        min_length = 0
        
        while right <= len(nums)-1:
            length = (right - left) + 1
            
            if cur_sum >= target:
                if min_length == 0 or length < min_length:
                    min_length = length
                    if min_length == 1:
                        return 1
                cur_sum -= nums[left]
                left += 1
                if left > right:
                    right += 1
        
            else: # cur_sum < target
                right += 1
                if right <= len(nums)-1:
                    cur_sum += nums[right]
                
        return min_length
                
                