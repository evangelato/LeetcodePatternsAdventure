# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev_node = None
        turtle = head
        rabbit = head.next

        while rabbit is not None:
            turtle.next = prev_node
            prev_node = turtle
            turtle = rabbit
            rabbit = rabbit.next

        turtle.next = prev_node
        return turtle
