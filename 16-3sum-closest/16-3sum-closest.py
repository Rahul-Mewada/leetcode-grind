'''
 -4 -1 1 2  -> target = 1
     i j k 
  
cur_sum = 2
closest = -1


 if cur_sum < target
    j += 1
 elif cur_sum > target
    k -= 1
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float(inf)
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                
                cur_sum = nums[i] + nums[j] + nums[k]

                if abs(target - cur_sum) < abs(target - closest_sum):
                    closest_sum = cur_sum
                
                if cur_sum < target:
                    j += 1
                elif cur_sum > target:
                    k -= 1
                else:
                    return nums[i] + nums[j] + nums[k]
                
        return closest_sum