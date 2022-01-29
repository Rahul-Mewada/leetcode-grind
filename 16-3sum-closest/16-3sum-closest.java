
// [-4, -1, 1, 2, 3, 4] target = 6
//       i        l   r  curSum = 6, curDiff = 1, difference = 1

//
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int difference = Integer.MAX_VALUE;
        int left;
        int right;
        int curSum;
        int curDiff;
        Arrays.sort(nums);
        
        
        
        for (int i = 0; i < nums.length-2; i++) {
            left = i+1;
            right = nums.length-1;
            
            
            while(left < right) {
                curSum = nums[i] + nums[left] + nums[right];
                curDiff = target - curSum;
                if(Math.abs(curDiff) < Math.abs(difference)) {
                    difference = curDiff;
                }
                
                
                if(curSum == target) {
                    return curSum;
                } else if(curSum > target) {
                    right--;
                } else {
                    left++;
                }
            }
        }
        
        
        return target - difference;
    }
}