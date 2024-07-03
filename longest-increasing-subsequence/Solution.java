// https://leetcode.com/problems/longest-increasing-subsequence

class Solution {
    public int lengthOfLIS(int[] nums) {
        int count = 1;
        int n = nums.length;

        int[] temp = new int[n];
        temp[0] = nums[0];

        for(int i = 1; i < n; i++){
            if (temp[count - 1] < nums[i]){
                temp[count++] = nums[i];
            } else {
                int index = Arrays.binarySearch(temp, 0, count, nums[i]);
                if (index < 0){
                    index = -(index + 1);
                }
                temp[index] = nums[i];
            }
        }
        
    return count;
    }
}