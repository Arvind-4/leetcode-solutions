// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

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

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        d = {}
        while head:
            if head.val in d:
                d[head.val] += 1
            else: d[head.val] = 1
            head = head.next

        for k, v in d.items():
            if v == 1:
                l.append(k)
        return self.convert(l)