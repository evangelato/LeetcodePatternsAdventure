# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_depth, max_diameter = self.dfs(root)
        return max_diameter

    def dfs(self, node) -> tuple[int, int]:
        if not node:
            return (0, 0)

        left_depth, left_max = self.dfs(node.left)
        right_depth, right_max = self.dfs(node.right)

        curr_diameter = left_depth + right_depth
        max_diameter = max(left_max, right_max, curr_diameter)
        max_depth = max(left_depth, right_depth)
        return (max_depth + 1, max_diameter)
