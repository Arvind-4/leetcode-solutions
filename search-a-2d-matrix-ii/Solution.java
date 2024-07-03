// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        int start = 0;
        int column = matrix[0].length;

        int end = column - 1;

        while(start < row && end >= 0){
            if (matrix[start][end] > target){
                end -= 1;
            }
            else if (matrix[start][end] < target){
                start += 1;
            }

            else {
                return true;
            }
        }
        return false;
    }
}