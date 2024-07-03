// https://leetcode.com/problems/sum-of-square-numbers

class Solution {
    public boolean judgeSquareSum(int c) {
        if (c < 0) return false;

        long left = 0;
        long right = (long) Math.sqrt(c);
        while (left <= right){
            long _sum = (left * left) + (right * right);
            if (_sum == c) return true;
            if (_sum > c) right -= 1;
            else left += 1;
        }
        return false;
    }
}