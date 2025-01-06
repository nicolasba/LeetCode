# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:    
        # first index: max depth of leftMostNode so far
        # second index: val of leftMostNode in max depth
        leftMostNode = [-1,-1]
        recFindBottomLeftValue(root, 0, leftMostNode)
        
        return leftMostNode[1]
    
def recFindBottomLeftValue(root, depth, leftMostNode):
    if root is None:
        return

    recFindBottomLeftValue(root.left, depth + 1, leftMostNode)
    recFindBottomLeftValue(root.right, depth + 1, leftMostNode)

    if depth > leftMostNode[0]:
        leftMostNode[0] = depth
        leftMostNode[1] = root.val
    

    