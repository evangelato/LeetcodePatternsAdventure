# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.findRoot(root, subRoot)

    def findRoot(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        if root.val == subRoot.val:
            found = self.dfsTogether(root, subRoot)
            if found:
                return True

        left_traversal = self.findRoot(root.left, subRoot)
        right_traversal = self.findRoot(root.right, subRoot)

        return left_traversal or right_traversal

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
