# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr_val = head.val
        turtle = head
        rabbit = head.next

        while rabbit is not None:
            if rabbit.val == curr_val:
                turtle.next = rabbit.next
                rabbit = rabbit.next
            else:
                curr_val = rabbit.val
                turtle = turtle.next
                rabbit = rabbit.next
        return head
