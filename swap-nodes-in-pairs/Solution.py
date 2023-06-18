// https://leetcode.com/problems/swap-nodes-in-pairs

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

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        n = len(l) & ~1
        l[1: n: 2],l[: n: 2] = l[: n: 2],l[1: n: 2]
        return self.convert(l)