#Inorder traversal
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
