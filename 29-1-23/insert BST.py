# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        a=root
        while True:
            if val<a.val and a.left is None:
                a.left=TreeNode(val)
                return root
            elif val>a.val and a.right is None:
                a.right=TreeNode(val)
                return root
            if val<a.val:
                a=a.left 
            elif val>a.val:
                a=a.right
