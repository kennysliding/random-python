# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfPath(node):
    if node.left is None and node.right is None:
        return [([node.val], node.val)]

    toReturn = []
    if node.left is not None:
        toReturn += [([node.val] + path[0], path[1] + node.val)
                     for path in sumOfPath(node.left)]
    if node.right is not None:
        toReturn += [([node.val] + path[0], path[1] + node.val)
                     for path in sumOfPath(node.right)]
    return toReturn


class Solution:

    def pathSum(self, root: Optional[TreeNode],
                targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        return [path[0] for path in sumOfPath(root) if path[1] == targetSum]