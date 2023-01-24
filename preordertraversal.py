#Preorder
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out=[]
        self.preorder(root,out)
        return out
    def preorder(self,root,out):
        if root:
            out.append(root.val)
            self.preorder(root.left,out)
            self.preorder(root.right,out)
