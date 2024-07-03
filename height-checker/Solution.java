// https://leetcode.com/problems/height-checker

import java.util.Arrays;

class Solution {
    public int heightChecker(int[] heights) {
        int n = heights.length;
        int count = 0;
        int expected[] = new int[n];
        for (int i = 0; i < n; i++){
            expected[i] = heights[i];
        }
        Arrays.sort(expected);
        for (int j = 0; j < n; j++){
            if (expected[j] != heights[j]){
                count += 1;
            }
        }
        return count;
    }
}