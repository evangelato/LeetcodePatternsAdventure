# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root

    def invert(self, node):
        if node == None:
            return
        tmp = node.right
        node.right = node.left
        node.left = tmp
        self.invert(node.right)
        self.invert(node.left)
