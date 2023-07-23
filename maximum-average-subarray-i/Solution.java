// https://leetcode.com/problems/maximum-average-subarray-i

class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double currentSum = 0, currentAvg = 0, maxAvg = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];
            if (i >= k - 1) {
                currentAvg = currentSum / k;
                maxAvg = Math.max(maxAvg, currentAvg);
                currentSum -= nums[i - (k - 1)];
            }
        }
        return maxAvg;

    }
}