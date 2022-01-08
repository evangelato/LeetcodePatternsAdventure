# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        rabbit = head.next
        turtle = head
        while rabbit is not None:
            if rabbit.val == val:
                turtle.next = rabbit.next
                rabbit = rabbit.next
            else:
                turtle = turtle.next
                rabbit = rabbit.next
        if head.val == val:
            head = head.next
        return head
