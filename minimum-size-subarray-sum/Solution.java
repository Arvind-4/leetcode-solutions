// https://leetcode.com/problems/minimum-size-subarray-sum

class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int answer = Integer.MAX_VALUE;
        int n = nums.length;
        int left = 0;
        int sum = 0;

        for (int right = 0; right < n; right++){
            sum += nums[right];

            while (sum >= target){
                sum -= nums[left];
                answer = Math.min(answer, right - left + 1);
                left += 1;
            }
        }

        if (answer == Integer.MAX_VALUE){
            return 0;
        }
        
        return answer;
    }
}