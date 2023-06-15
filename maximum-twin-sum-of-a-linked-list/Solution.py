// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        while head:
            l.append(head.val)
            head = head.next

        maxx = l[0]
        n = len(l)
        for i in range(n // 2):
            summ = l[i] + l[n - i -1]
            maxx = max(summ, maxx)
        return maxx