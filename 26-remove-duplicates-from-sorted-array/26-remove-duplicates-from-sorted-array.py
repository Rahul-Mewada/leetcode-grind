"""
 
 1  
i  j
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        j = 1
        
        for i in range(len(nums) - 1):
            while j < len(nums) and nums[j] == nums[i]:
                nums.pop(j)
            j += 1