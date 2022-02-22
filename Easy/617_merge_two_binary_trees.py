# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        return self.dfsMerge(root1, root2)

    def dfsMerge(self, node1, node2) -> bool:
        if node1 == None and node2 == None:
            return None
        if node1 == None:
            return node2
        if node2 == None:
            return node1

        sum = node1.val + node2.val

        left_node = self.dfsMerge(node1.left, node2.left)
        right_node = self.dfsMerge(node1.right, node2.right)

        new_node = TreeNode(sum, left_node, right_node)

        return new_node
