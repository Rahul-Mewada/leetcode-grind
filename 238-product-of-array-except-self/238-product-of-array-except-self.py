'''

suf = 8
n- 1  2  3  4  2
p- 1  1  2  6  24
      i
r-       16  12  24 

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_pro = [None] * (len(nums))
        left_pro[0] = 1
        
        for i in range(1, len(nums)):
            left_pro[i] = nums[i-1] * left_pro[i-1]
        
        suf = 1

        
        for i in reversed(range(len(left_pro))):
            left_pro[i] = left_pro[i] * suf
            suf *= nums[i]
        
        return left_pro