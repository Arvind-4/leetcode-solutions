// https://leetcode.com/problems/find-the-pivot-integer

class Solution {
    public int pivotInteger(int n) {
        int total = 0;
        int curr = 0;

        for (int i = 1; i <= n; i++){
            total += i;
        }

        for (int i = 1; i <= n; i++){
            if(curr + i == total){
                return i;
            }
            total -= i;
            curr += i;
        }

        return -1;
        
    }
}