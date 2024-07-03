// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                nums.append(matrix[i][j])

        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return 1
            elif nums[mid] > target:
                end = mid -1
            else:
                start = mid + 1
        if nums[start] == target: return True
        return 0
        