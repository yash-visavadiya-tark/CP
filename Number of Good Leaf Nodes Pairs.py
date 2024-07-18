# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0
        self.is_leaf_found = False
        self.d = 0

    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaf_nodes = []
        self.fill_leaf_nodes(root, leaf_nodes)

        for leaf_node in leaf_nodes:
            self.is_leaf_found = False
            self.d = 0
            self.helper(root, leaf_node, distance)
        return self.ans

    def fill_leaf_nodes(self, root, leaf_nodes):
        if root:
            if root.left:
                self.fill_leaf_nodes(root.left, leaf_nodes)
            if root.right:
                self.fill_leaf_nodes(root.right, leaf_nodes)
            if root.left is None and root.right is None:
                leaf_nodes.append(root)

    def helper(self, root: TreeNode, leaf_node, distance: int):
        if root and self.d <= distance:
            if root.left:
                if self.is_leaf_found:
                    previous_d = self.d
                    self.d += 1
                    self.helper(root.left, leaf_node, distance)
                    self.d = previous_d
                else:
                    self.helper(root.left, leaf_node, distance)

            if root.right:
                if self.is_leaf_found:
                    previous_d = self.d
                    self.d += 1
                    self.helper(root.right, leaf_node, distance)
                    self.d = previous_d
                else:
                    self.helper(root.right, leaf_node, distance)

            if root.left is None and root.right is None:
                if self.is_leaf_found:
                    if self.d <= distance:
                        self.ans += 1
                if root == leaf_node:
                    self.is_leaf_found = True

            if self.is_leaf_found:
                self.d += 1

    
if __name__ == '__main__':
    print(Solution().countPairs(
        # TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))), 3)
        # TreeNode(43, TreeNode(32, TreeNode(72), TreeNode(34, None, TreeNode(70))), TreeNode(22, None, TreeNode(28))),
        # 3)
        TreeNode(78, TreeNode(15, TreeNode(73, TreeNode(30)), TreeNode(98, TreeNode(63), TreeNode(32))),
                 TreeNode(81, TreeNode(36))),
        6)
    )
