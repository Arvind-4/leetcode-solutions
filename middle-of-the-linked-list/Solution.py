// https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        n = 0
        while head:
            l.append(head)
            n += 1
            head = head.next
        k = n // 2 if n % 2 else int(n/2)
        return l[k]
