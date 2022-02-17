class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        
        if(nums.length == 1) {
            if(nums[0] == target) return 0;
            return -1;
        }
        
        while(left <= right) {
            int mid = (right + left)/2;
            if(nums[mid] == target) {
                return mid;
            } else if(nums[mid] < target) {
                // look right
                left = mid + 1;
            } else {
                // look left
                right = mid - 1;
            } 
        }
        
        return -1;
    }
}