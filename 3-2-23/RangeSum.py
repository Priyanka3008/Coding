# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def range(self,root,low,high,s):
        if root is None:
            return s
        if root.val>=low and  root.val<=high:
            s+=root.val
        s=self.range(root.left,low,high,s)
        s=self.range(root.right,low,high,s)
        return s
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
         return self.range(root,low,high,0)
