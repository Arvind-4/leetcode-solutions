// https://leetcode.com/problems/arranging-coins

class Solution {
    public int arrangeCoins(int n) {

        long left = 1;
        long right = n;
        int ans = -1;


        while (left <= right){
            long mid = left + (right - left) / 2;
            long stairs = (mid * (mid + 1)) / 2;

            if (stairs <= n){
                ans = (int)mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return ans;
    }
}