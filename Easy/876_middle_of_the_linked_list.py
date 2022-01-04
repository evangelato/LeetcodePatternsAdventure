# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabbit = head
        turtle = head

        while rabbit is not None and rabbit.next is not None:
            rabbit = rabbit.next.next
            turtle = turtle.next
        return turtle


class HashSolution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        loc_dict = {}
        curr_node = head
        count = 0
        while curr_node is not None:
            loc_dict[count] = curr_node
            curr_node = curr_node.next
            count += 1

        mid_index = count // 2
        return loc_dict[mid_index]
