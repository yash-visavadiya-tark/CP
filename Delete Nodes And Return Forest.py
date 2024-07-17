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

        if root.left and root.left.val in to_delete:
            if root.left.left and root.left.left.val not in to_delete:
                forest.append(root.left.left)
            if root.left.right and root.left.right.val not in to_delete:
                forest.append(root.left.right)
            self.helper(root.left, forest, to_delete)
            root.left = None

        if root.right and root.right.val in to_delete:
            if root.right.left and root.right.left.val not in to_delete:
                forest.append(root.right.left)
            if root.right.right and root.right.right.val not in to_delete:
                forest.append(root.right.right)
            self.helper(root.right, forest, to_delete)
            root.right = None

        if root.left:
            self.helper(root.left, forest, to_delete)
        if root.right:
            self.helper(root.right, forest, to_delete)


if __name__ == "__main__":
    print(Solution().delNodes(
        TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))),
        [3, 5]))  #
