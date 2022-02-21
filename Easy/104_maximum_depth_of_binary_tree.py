# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_depth = self.dfs(root, 0)
        return max_depth

    def dfs(self, node, depth) -> int:
        new_depth = depth + 1
        if node.left == None and node.right == None:
            return new_depth
        elif node.left == None:
            max_depth = self.dfs(node.right, new_depth)
        elif node.right == None:
            max_depth = self.dfs(node.left, new_depth)
        else:
            left_depth = self.dfs(node.left, new_depth)
            right_depth = self.dfs(node.right, new_depth)
            max_depth = max(left_depth, right_depth)
        return max_depth
