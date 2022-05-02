'''
n- 1  2  3  4
p- 1  2  6  24
s- 24 24 12  4

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [None] * len(nums)
        suf = [None] * len(nums)
        products = [None] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                pre[i] = nums[i]
            else:
                pre[i] = nums[i] * pre[i-1]
        
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                suf[i] = nums[i]
            else:
                suf[i] = nums[i] * suf[i+1]
        
        for i in range(len(products)):
            if i == 0:
                products[i] = suf[i+1]
            elif i == len(products) - 1:
                products[i] = pre[i-1]
            else:
                products[i] = suf[i+1] * pre[i-1]
        
        return products
            