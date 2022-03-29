'''
 16 1 0 9 100
 n      p
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_sq = []
        i = 0 
        while i < len(nums):
            if nums[i] >= 0:
                break
            i += 1
        
        neg = i - 1
        pos = i
        
        while pos < len(nums) and neg >= 0:
            print(nums[pos], nums[neg])
            sq_pos = nums[pos] * nums[pos]
            sq_neg = nums[neg] * nums[neg]
            
            if sq_pos > sq_neg:
                sorted_sq.append(sq_neg)
                neg -= 1
            else:
                sorted_sq.append(sq_pos)
                pos += 1
        
        while pos < len(nums):
            sorted_sq.append(nums[pos] * nums[pos])
            pos += 1
        while neg >= 0:
            sorted_sq.append(nums[neg] * nums[neg])
            neg -= 1
            
        return sorted_sq