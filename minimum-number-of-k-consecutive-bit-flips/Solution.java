// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips

class Solution {
    public int minKBitFlips(int[] nums, int k) {
        int n = nums.length;
        int[] fp = new int[n];
        int flipped = 0;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (i >= k){
                flipped ^= fp[i - k];
            }
            if (flipped == nums[i]) {
                if (i + k > n){
                    return -1;
                }
                fp[i] = 1;
                flipped ^= 1;
                ans += 1;
            }
        }
        return ans;
    }
}