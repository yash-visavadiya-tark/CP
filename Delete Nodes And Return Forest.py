from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = []
        head = TreeNode(-1, root)

        if root.val not in to_delete:
            forest.append(root)

        self.helper(head, forest, to_delete)
        return forest

    def helper(self, root: Optional[TreeNode], forest: List[TreeNode], to_delete: List[int]):
        if not root:
            return

        if self.is_in_to_delete_then_process(root.left, forest, to_delete):
            root.left = None
        else:
            self.helper(root.left, forest, to_delete)

        if self.is_in_to_delete_then_process(root.right, forest, to_delete):
            root.right = None
        else:
            self.helper(root.right, forest, to_delete)

    def is_in_to_delete_then_process(self, node, forest, to_delete):
        if node and node.val in to_delete:
            if node.left and node.left.val not in to_delete:
                forest.append(node.left)
            if node.right and node.right.val not in to_delete:
                forest.append(node.right)
            self.helper(node, forest, to_delete)
            return True
        return False


if __name__ == "__main__":
    print(Solution().delNodes(
        TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))),
        [3, 5]))  #
