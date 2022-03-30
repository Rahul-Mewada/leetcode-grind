'''
[
 -1 -1  2
 -1  0  1
 
]

 -1 -1 0 1 1 1 2 2 2 
       i j         k          
  
  cur = -1
  target = 1
  inner = 1
  
  if inner < target:
    j++
  else 
    k--
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        triplets = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
                
            if nums[i] > 0:
                break
                
            cur_sum = nums[i]
            j = i + 1
            k = len(nums) - 1
            target = -cur_sum
            
            while j < k:
                inner = nums[j] + nums[k]
                if inner < target:
                    j += 1
                elif inner > target:
                    k -= 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -=1 
                    while j < k and  nums[j-1] == nums[j]:
                        j += 1
                    
                    while j < k and  nums[k+1] == nums[k]:
                        k -= 1
        return triplets