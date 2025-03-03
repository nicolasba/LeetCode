# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        path = []

        # Even numbers are always the right child
        # Odd numbers are always the left child
        # So reconstruct path to get to target in reverse
        while target > 0:
            if target % 2 == 0:
                path.append("right")
                target = (target - 2) / 2
            else: 
                path.append("left")
                target = (target - 1) / 2

        # Follow constructed path above
        tmp = self.root
        for p in path[::-1]:
            if p == "right":
                if tmp.right is None:
                    return False
                tmp = tmp.right
            else:
                if tmp.left is None:
                    return False
                tmp = tmp.left
        
        return True

        
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)