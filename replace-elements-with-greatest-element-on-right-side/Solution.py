// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        m = -1

        for i in range(n - 1, -1, -1):
            if arr[i] > m:
                m, arr[i] = arr[i], m
            else:
                arr[i] = m
        return arr