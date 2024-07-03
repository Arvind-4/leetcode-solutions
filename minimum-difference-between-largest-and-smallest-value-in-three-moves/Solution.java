// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves

class Solution {
    public int minDifference(int[] nums) {
        int n = nums.length;
        if (n <= 4) return 0;
        Arrays.sort(nums);
        int l = 0;
        int r = n - 4;
        int res = nums[r] - nums[l];

        while (r < n){
            res = Math.min(res, nums[r] - nums[l]);
            l += 1;
            r += 1;
        }

        return res;
    }
}