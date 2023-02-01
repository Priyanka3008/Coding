# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        row,col=0,0
        val={}
        result=[]
        self.vertical(root,row,col,val)
        for i in sorted(val.keys()):
            l=[j[1] for j in sorted(val[i])]
            result.append(l)
        return result
    def vertical(self,root,row,col,val):
            if root is None:
                return None
            if col in val:
                val[col].append((row,root.val))
            else:
                val[col]=[(row,root.val)]
            self.vertical(root.left,row+1,col-1,val)
            self.vertical(root.right,row+1,col+1,val)
