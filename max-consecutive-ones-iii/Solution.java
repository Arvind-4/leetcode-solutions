// https://leetcode.com/problems/max-consecutive-ones-iii

class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0, right = 0;
        int n = nums.length;

        while (right < n && k > 0) {
            if (nums[right] == 0) {
                k -= 1;
            }
            right += 1;
            if (right == n) {
                return n;
            }
        }
        int len = right - left;

        while(right < n) {
            if (nums[right] == 1) {
                right += 1;
                len = Math.max(len, right - left);
            } else {
                while(nums[left] == 1){
                    left += 1;
                }
                left += 1;
                right += 1;
            }
        }

        return len;
    }
}