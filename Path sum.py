# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check(root,cursum):
            if root is None:
                return 0
            cursum+=root.val
            if not root.left and not root.right:
                return cursum==targetSum
            l=check(root.left,cursum)
            r=check(root.right,cursum)
            return l or r
        return check(root,0)
       
