// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter

class Solution {
    public long largestPerimeter(int[] nums) {
        Arrays.sort(nums);

        long n = nums.length;
        long sum = nums[0] + nums[1];
        long res = 0;

        for (int i = 2; i < nums.length; i++){
            if (sum > nums[i]){
                res = sum + nums[i];
            }
            sum += nums[i];
        }
        if (res == 0) return -1;
        return res;
    }
}