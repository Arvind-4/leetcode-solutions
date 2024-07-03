// https://leetcode.com/problems/three-consecutive-odds

class Solution {
    public boolean checkOdd(int num){
        if (num % 2 != 0) return true;
        return false;
    }
    public boolean threeConsecutiveOdds(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n - 2; i++){
            boolean val1 = checkOdd(arr[i]);
            boolean val2 = checkOdd(arr[i + 1]);
            boolean val3 = checkOdd(arr[i + 2]);
            if (val1 && val2 && val3) return true;
        }
        return false;
    }
}