# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root, 0))

        isLeftMost = True
        prevLevel = 0
        prevVal = 0

        while q:
            node, level = q.popleft()

            evenLevel = level % 2 == 0
            isLeftMost = prevLevel != level

            if evenLevel:
                if node.val % 2 == 0:
                    return False
                if not isLeftMost and node.val <= prevVal:
                    return False
            else:
                if node.val % 2 == 1:
                    return False
                if not isLeftMost and node.val >= prevVal:
                    return False

            prevLevel = level
            prevVal = node.val

            if node.left is not None:
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))

        return True