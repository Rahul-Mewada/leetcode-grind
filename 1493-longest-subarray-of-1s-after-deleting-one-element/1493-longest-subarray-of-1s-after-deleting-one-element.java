class Solution {
    public int longestSubarray(int[] nums) {
        // [0,1,1,1,0,1,1,0,1]
        //    j         r
        //  c - 1
        int left = 0;
        int count = 0;
        int length = 0;
        if(nums[left] == 0) {
            count++;
        }
        
        for(int right = 1; right < nums.length; right++) {
            if(nums[right] == 0) {
                count++;
            }
            
            while(count > 1) {
                if(nums[left] == 0) {
                    count--;
                }
                left++;
            }
            
            length = Math.max((right - left), length);
           
                        
            
        }
        
        return length;
    }
}