# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self,root: Optional[TreeNode]) -> List[int]:
        out=[]
        self.inorder(root,out)
        return out
    def inorder(self,root,out):
        if root:
            self.inorder(root.left,out)
            out.append(root.val)
            self.inorder(root.right,out)
        
