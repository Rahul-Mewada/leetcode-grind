/*

[1, 2, 3, 4]    t = 0  result = 3
 lr      
 m
*/       

class Solution {
    public int searchInsert(int[] nums, int target) {
        
        if(nums.length == 1) {
            if(target <= nums[0]) return 0;
            return 1;
        }
        
        return binSearch(nums, target, 0, nums.length - 1);
    }
    
    public int binSearch(int[] nums, int target, int left, int right) {
        int mid = 0;
        
        while(left <= right) {
            mid = left + (right - left)/2;
            if(nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        if(nums[mid] < target) {
            return mid + 1;
        } else {
            return mid;
        }
        
    }
}