# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        min_depth = self.dfs(root, 0)
        return min_depth

    def dfs(self, node, depth) -> int:
        new_depth = depth + 1
        if node.left == None and node.right == None:
            return new_depth
        elif node.left == None:
            min_depth = self.dfs(node.right, new_depth)
        elif node.right == None:
            min_depth = self.dfs(node.left, new_depth)
        else:
            left_depth = self.dfs(node.left, new_depth)
            right_depth = self.dfs(node.right, new_depth)
            min_depth = min(left_depth, right_depth)
        return min_depth
