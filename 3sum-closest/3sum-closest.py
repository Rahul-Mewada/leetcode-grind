'''
[-4, -1, 1, 2]
  i   i  l  r
1) Sort the array
2) Start a loop 
3) Inside the loop initiate two pointers
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) <= 3:
            result = 0
            for num in nums:
                result += num
            return result
        
        nums.sort()
        diff = 100000
        result = diff
        
        for index, num in enumerate(nums):
            left = index+1
            right = len(nums)-1
            while left < right:
                summ = num + nums[left] + nums[right]
                if abs(summ - target) <= diff:
                    result = summ
                    diff = abs(summ - target)
                if summ > target:
                    right -= 1
                elif summ < target:
                    left += 1
                else:
                    return summ
        return result
                