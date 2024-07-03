// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x

class Solution {
    public int specialArray(int[] nums) {
        int x = nums.length;
        int[] counts = new int[x + 1];

        for(int el : nums){
            if (el >= x){
                counts[x]++;
            } else {
                counts[el]++;
            }
        }
        int res = 0;
        for (int i = counts.length - 1; i > 0; i--){
            res += counts[i];
            if(res == i){
                return i;
            }
        }
        return -1;
    }
}