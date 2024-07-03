// https://leetcode.com/problems/score-of-a-string

class Solution {
    public int scoreOfString(String s) {
        int n = s.length();
        int sum = 0;
        for (int i = 1; i < n; i++){
            char first = s.charAt(i - 1);
            char second = s.charAt(i);
            System.out.println((int) first);
            System.out.println((int) second);
            sum += Math.abs(((int) first) - ((int) second));
        }

        return sum;
    }
}