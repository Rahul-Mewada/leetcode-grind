'''
[3]
sf
 
min_len = 0

cur_sum = 7
target = 7
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        cur_sum = 0
        slow = 0
        for fast in range(len(nums)):
            cur_sum += nums[fast]
            while(cur_sum >= target):
                min_len = min(min_len, fast - slow + 1)
                cur_sum -= nums[slow]
                slow += 1
        return 0 if min_len == float('inf') else min_len