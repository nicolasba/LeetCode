# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        recFlatten(root)

def recFlatten(node):
    if node is not None:
        if node.right is not None:
            recFlatten(node.right)
        if node.left is not None:
            recFlatten(node.left)
        if node.left is not None:
            rightmostNode = recRightmostNode(node.left)
            rightmostNode.right = node.right
            node.right = node.left
            node.left = None

def recRightmostNode(node):
    if node.right is not None:
        return recRightmostNode(node.right)
    else:
        return node
    
        