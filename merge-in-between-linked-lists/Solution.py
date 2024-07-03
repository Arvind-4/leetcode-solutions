// https://leetcode.com/problems/merge-in-between-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convert(self, l: List[int]) -> ListNode:
        current = sample = ListNode(0)
        for el in l:
            current.next = ListNode(el)
            current = current.next
        return sample.next

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1, l2 = [], []
        while list1:
            l1.append(list1.val)
            list1 = list1.next
        while list2:
            l2.append(list2.val)
            list2 = list2.next
        l1[a: b + 1] = l2[:]
        return self.convert(l1)