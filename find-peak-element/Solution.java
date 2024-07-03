// https://leetcode.com/problems/find-peak-element

class Solution {
    public int findPeakElement(int[] nums) {

        int index = 0;
        int max = nums[0];

        for (int i = 0; i < nums.length; i++){
            if(nums[i] > max){
                max = nums[i];
                index = i;
            }
        }

        return index;

        
    }
}