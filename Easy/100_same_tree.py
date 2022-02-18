# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return self.dfsTogether(p, q)

    def dfsTogether(self, p, q) -> bool:
        if p == None and q == None:
            return True
        if p == None:
            return False
        if q == None:
            return False
        if p.val != q.val:
            return False

        left_together = self.dfsTogether(p.left, q.left)
        right_together = self.dfsTogether(p.right, q.right)

        return left_together and right_together
