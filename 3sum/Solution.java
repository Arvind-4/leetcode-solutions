// https://leetcode.com/problems/3sum

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;

        Arrays.sort(nums);

        Set<List<Integer>> ans = new HashSet<>();
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < n; i++){
            int j = i + 1;
            int k = n - 1;
            while (j < k){
                int summ = nums[i] + nums[j] + nums[k];
                if (summ == 0){
                    ans.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j += 1;
                    k -= 1;
                }
                else if (summ > 0) k-= 1;
                else j += 1;
            }
        }
        res.addAll(ans);
        return res;
    }
}