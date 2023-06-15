// https://leetcode.com/problems/add-two-numbers-ii

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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1, list2 = [], []

        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        num1 = int("".join(map(str, list1)))
        num2 = int("".join(map(str, list2)))
        summ = str(num1 + num2)
        l = list(map(int, list(summ)))
        return self.convert(l)