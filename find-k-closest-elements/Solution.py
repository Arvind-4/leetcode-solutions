// https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        h = len(arr) - k

        while l < h:
            mid = (h + l) // 2
            if x <= arr[mid]:
                h = mid
            elif arr[mid + k] <= x:
                l = mid + 1
            else:
                middist = abs(x - arr[mid])
                midkdist = abs(x - arr[mid + k])
                if middist <= midkdist:
                    h = mid
                else: l = mid + 1
        return arr[l: l + k]