// https://leetcode.com/problems/remove-duplicates-from-sorted-list

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
        while head:
            l.append(head.val)
            head = head.next
        l = sorted(list(set(l)))
        print(l)

        return self.convert(l)