'''
Three sum problem 

1) sort the array - O(n log n)
2) start a loop
3) Nest the two pointers in that loop
4) Keep track of the sum closest to the target

[-4, -2, -1, 0] target = 1   
  i   l      r
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        last_sum = None
        print(nums)
        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            
            while left < right:
                three_sum = num + nums[left] + nums[right]      
                cur_error = abs(target - three_sum)                 
                if last_sum != None: 
                    last_error = abs(target - last_sum)
                    if cur_error < last_error:
                        last_sum = three_sum
                else:
                    last_sum = three_sum                            
                    
                if three_sum == target:
                    return target
                elif three_sum < target:
                    left += 1
                else:
                    right -= 1
                print(last_sum) 
                print()
                    
              
               
        return last_sum