# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        return self.dfs(root, p, q)[0]

    def dfs(
        self, search_node: "TreeNode", node1: "TreeNode", node2: "TreeNode"
    ) -> tuple["TreeNode", bool]:
        if search_node is None:
            return (None, False)

        left_traversal = self.dfs(search_node.left, node1, node2)
        right_traversal = self.dfs(search_node.right, node1, node2)

        found = left_traversal[1] or right_traversal[1]
        return_node = left_traversal[0] or right_traversal[0]

        if left_traversal[1] and right_traversal[1]:
            return_node = search_node

        if search_node == node1 or search_node == node2:
            if found:
                return_node = search_node
            else:
                found = True

        return return_node, found
