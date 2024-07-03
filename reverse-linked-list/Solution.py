// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convert(self, l: List[int]) -> Optional[ListNode]:
        current = sample = ListNode(0)
        for el in l:
            current.next = ListNode(el)
            current = current.next
        return sample.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.reverse()
        return self.convert(l)
