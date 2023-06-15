// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convert(self, arr: List[int]) -> Optional[ListNode]:
        current = sample = ListNode(0)
        for ele in arr:
            current.next = ListNode(ele)
            current = current.next
        return sample.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.pop(len(l) - n)
        return self.convert(l)