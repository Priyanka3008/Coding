# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.height(root.left)-self.height(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self,root):
        if root is None:
            return 0
        l=self.height(root.left)
        r=self.height(root.right)
        return max(l,r)+1
