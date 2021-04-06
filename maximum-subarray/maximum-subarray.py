'''
Kadanes? Algorithm
(Sliding window O(N) time and O(1) space complexity)

cur_sum= -1
prev_sum= -2
max_sum= -1
[-2,1,-3,4,-1,2,1,-5,4]
  l    r

if cur_sum > prev_sum: right += 1
else: left += 1 if left > right: right += 1

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)