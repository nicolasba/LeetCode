# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return recIsBalanced(root, 0) != -1
        
def recIsBalanced(node, depth):
    if node is None:
        return depth

    left_depth = recIsBalanced(node.left, depth + 1)
    right_depth = recIsBalanced(node.right, depth + 1)

    if left_depth == -1 or right_depth == -1:
        return -1

    if abs(left_depth - right_depth) > 1:
        return -1 
    
    return max(left_depth, right_depth)
