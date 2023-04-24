// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        answer = set()
        count = 0
        while(count < len(nums)):
            if(nums[count] in answer):
                nums.remove(nums[count])
            else:
                answer.add(nums[count])
                count += 1

        return len(answer)
            