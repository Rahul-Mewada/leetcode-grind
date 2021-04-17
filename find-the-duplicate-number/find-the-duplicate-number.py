'''
1) length of the array == n+1
2) all elements are in the range [1, n]
3) only one repeated number

Approach 1) - Dump into a hashset -> O(N) time and space complexity 

Approach 2) 
[1, 3, 4, 2, 2]
[1, 2, 2, 3, 4]
Sort it 
[1, 2, 2, 2, 3, 4, 5]     
 l        m        r
 
modified binary search 

looking at the mid point 
1) if val > index: look right
2) if val <= index: look left
    
    
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        mid = 0
        print(nums)
        while left < right-1:
            mid = (left+right)//2
            val = nums[mid]
            print((nums[left], nums[right]))
            print(nums[mid])
            print()
            index = mid+1
            if val < index:
                right=mid
            else:
                left=mid
        return nums[mid]