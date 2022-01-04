# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rabbit = head
        turtle = head
        turtle_history = []

        while rabbit is not None and rabbit.next is not None:
            rabbit = rabbit.next.next
            turtle_history.append(turtle.val)
            turtle = turtle.next

        if rabbit is not None:
            # Odd
            turtle = turtle.next

        while turtle is not None:
            if turtle.val != turtle_history[-1]:
                return False
            turtle_history.pop()
            turtle = turtle.next

        return True
