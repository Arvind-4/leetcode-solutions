// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listToLinkedList(self, arr: List[int]) -> Optional[ListNode]:
        current = sample = ListNode(0)
        for element in arr:
            current.next = ListNode(element)
            current = current.next
        return sample.next

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        index = len(l) // 2
        l.pop(index)
        return self.listToLinkedList(l)