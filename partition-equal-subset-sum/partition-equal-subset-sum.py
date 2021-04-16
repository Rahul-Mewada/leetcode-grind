'''
[1, 5, 11, 5]
total_sum = 1 + 5 + 11 + 5 = 22
target = 11
current_sum = 11

                                          []
                    1               5              11              5
            5       11      5       11     5        5     
        11.  5.     5
     5
     
Combinatorics using the Subset Pattern
1) Type of DFS
2) Keep a running sum and keep track of the target which is the total of all the elements in the array
3) Each function call, add a new unique element to the running total
4) If the running total is greater than the target, terminate that particular path
5) keep track of which index you're adding


[1, 3, 2] target = 3

'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        target = 0
        for num in nums: 
            target += num
        if target%2 != 0:
            return False
        target /= 2
        mem = {}
        return self.combinations(nums, -1, target, mem)
        
    def combinations(self, nums, index, target, mem):
        if target in mem:
            return mem[target]
        
        if target == 0:
            mem[target] = True
            return True
        else:
            mem[target] = False
            if target > 0:
                for i in range(index+1, len(nums)):
                    can_partition = self.combinations(nums, i, target-nums[i], mem)
                    if can_partition: 
                        mem[target] = True
                        return True
            
        return mem[target]