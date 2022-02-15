# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        return_list = []

        parent_queue = [root]
        child_queue = []

        while parent_queue:
            count = 0
            total = 0
            for node in parent_queue:
                count += 1
                total += node.val
                if node.left:
                    child_queue.append(node.left)
                if node.right:
                    child_queue.append(node.right)

            avg = total / count
            return_list.append(avg)

            parent_queue = child_queue
            child_queue = []

        return return_list
