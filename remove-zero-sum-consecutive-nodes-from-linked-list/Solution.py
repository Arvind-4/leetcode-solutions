// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        summ = 0
        d = {}
        test = ListNode(0)
        test.next = head

        d[0] = test

        while head:
            summ += head.val
            if summ in d:
                start = d[summ]
                temp = start
                pSum = summ

                while temp != head:
                    temp = temp.next
                    pSum += temp.val
                    if temp != head:
                        del d[pSum]
                start.next = head.next

            else: d[summ] = head
            head = head.next
        return test.next