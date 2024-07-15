from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root = descriptions[0][0]

        _children_map = defaultdict(list)
        _cnt_map = defaultdict(int)

        for parent, child, isLeft in descriptions:
            _children_map[parent].append([parent, child, isLeft])
            _cnt_map[child] += 1

        for parent, child, isLeft in descriptions:
            if _cnt_map[parent] == 0:
                root = parent
                break

        return self.helper(TreeNode(root), descriptions, _children_map)

    def helper(self, curr, descriptions, _children_map):
        if not curr:
            return None

        data = _children_map[curr.val]

        for parent, child, isLeft in data:
            if isLeft:
                curr.left = TreeNode(child)
                self.helper(curr.left, descriptions, _children_map)
            else:
                curr.right = TreeNode(child)
                self.helper(curr.right, descriptions, _children_map)

        return curr

    def optimized(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        child = set()

        for p, c, l in descriptions:
            if p in d:
                p = d[p]
            else:
                d[p] = TreeNode(p)
                p = d[p]

            child.add(c)
            if c in d:
                c = d[c]
            else:
                d[c] = TreeNode(c)
                c = d[c]

            if l:
                p.left = c
            else:
                p.right = c

        for p, _, _ in descriptions:
            if p not in child:
                return d[p]
