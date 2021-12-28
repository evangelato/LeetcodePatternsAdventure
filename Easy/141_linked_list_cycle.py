# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit = head
        turtle = head
        while rabbit is not None and rabbit.next is not None:
            rabbit = rabbit.next.next
            turtle = turtle.next
            if rabbit == turtle:
                return True
        return False


class HashSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = {}
        curr_node = head
        while curr_node is not None and curr_node.next is not None:
            if curr_node.next.val in seen_nodes:
                if curr_node.next in seen_nodes[curr_node.next.val]:
                    return True
                else:
                    seen_nodes[curr_node.next.val].append(curr_node)
                    curr_node = curr_node.next
            else:
                seen_nodes[curr_node.val] = [curr_node]
                curr_node = curr_node.next
        return False
