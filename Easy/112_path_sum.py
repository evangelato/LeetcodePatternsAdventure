# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return self.dfsSum(root, targetSum, 0)

    def dfsSum(self, node, targetSum, totalSum) -> bool:
        newSum = totalSum + node.val
        if not node.left and not node.right:
            if targetSum == newSum:
                return True
            else:
                return False

        left_traversal = False
        right_traversal = False
        if node.left:
            left_traversal = self.dfsSum(node.left, targetSum, newSum)
        if node.right:
            right_traversal = self.dfsSum(node.right, targetSum, newSum)

        return left_traversal or right_traversal
