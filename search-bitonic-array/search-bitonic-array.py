'''
Find an element in Bitonic array: Medium

Given a bitonic sequence of n distinct elements, write a program to find a given element x in the bitonic 
sequence in O(log n) time. A Bitonic Sequence is a sequence of numbers that is first strictly increasing 
then after a point strictly decreasing.

Examples: 
Input :  arr[] = {-3, 9, 18, 20, 17, 5, 1};
         key = 20
Output : Found at index 3

Input :  arr[] = {5, 6, 7, 8, 9, 10, 3, 2, 1};
         key = 30
Output : Not Found
'''

def search_arr(nums, target):

    return find_partition(nums, target, 0, len(nums)-1)
    
def find_partition(nums, target, left, right):
    if left > right:
        return -1

    
    mid = (left + right)//2
    if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
        left_index = bin_search(nums[0: mid], target, 0, mid-1, False)
        right_arr = nums[mid: len(nums)] 
        right_index = bin_search(right_arr, target, 0, len(right_arr)-1, True)
        return max(left_index, right_index)
    elif nums[mid-1] < nums[mid] < nums[mid+1]:
        return find_partition(nums, target, mid, right)
    elif nums[mid-1] > nums[mid] > nums[mid+1]:
        return find_partition(nums, target, left, mid)

    
    
def bin_search(nums, target, left, right, is_rev):
    if left > right:
        return -1

    mid = (left+right)//2

    if not is_rev:
        if nums[mid] < target:
            return bin_search(nums, target, mid, right, is_rev)
        elif nums[mid] > target:
            return bin_search(nums, target, left, mid, is_rev)
        else:
            return mid
    else:
        if nums[mid] > target:
            return bin_search(nums, target, mid, right, is_rev)
        elif nums[mid] < target:
            return bin_search(nums, target, left, mid, is_rev)
        else:
            return mid

def main():
    nums = [5, 6, 7, 8, 9, 10, 3, 2, 1]
    target = 1
    output = len(nums) -1

    ans = search_arr(nums, target)

    print(output == ans)
    print("Your answer: " + str(ans))
    print("Expected: " + str(output))
    print(nums)
if __name__ == "__main__":
    main()