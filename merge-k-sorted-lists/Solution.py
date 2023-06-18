// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convert(self, arr: List[int]) -> Optional[ListNode]:
        current = sample = ListNode(0)
        for el in arr:
            current.next = ListNode(el)
            current = current.next
        return sample.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for head in lists:
            while head:
                l.append(head.val)
                head = head.next
        return self.convert(sorted(l))
