from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        depth = self.get_depth(root)
        row = depth
        col = 2 ** depth - 1
        res = [['' for _ in range(col)] for _ in range(row)]

        def dfs(node, row, left, right):
            if node is None:
                return

            mid = (left + right) // 2
            res[row][mid] = str(node.val)
            dfs(node.left, row + 1, left, mid - 1)
            dfs(node.right, row + 1, mid + 1, right)

        dfs(root, 0, 0, col - 1)

        return res

    def get_depth(self, root):
        if root is None:
            return 0

        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))


if __name__ == '__main__':
    s = Solution()

    # Example 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    print(s.printTree(root))
    # Output: [["", "", "", "1", "", "", ""], ["", "2", "", "", "", "3", ""], ["", "", "4", "", "", "", ""]]

    # Example 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    print(s.printTree(root))
