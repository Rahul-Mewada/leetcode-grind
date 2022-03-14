"""
 2 3 4 5 
 
 
 
 target.= 5
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]].append(i)
            else:
                freq[nums[i]] = [i]
    
        for i in range(len(nums)):
            rem = target - nums[i]
            
            if rem in freq:
                value = freq[rem]
                if rem == nums[i] and len(value) > 1:
                    return [value[0], value[1]]
                elif rem == nums[i] and len(value) == 1:
                    continue
                else:
                    return [i, value[0]]
                    
            