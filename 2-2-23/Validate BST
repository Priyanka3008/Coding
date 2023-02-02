# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l=[]
        self.inorder(root,l)
        for i in range(1,len(l)):
            if l[i-1]>=l[i]:
                return False
        return True
    def inorder(self,root,l):
            if root is None:
                return
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)

        
