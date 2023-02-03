# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        def inorder(root,d):
            if not root:
                return
            inorder(root.left,d)
            d[root.val]=d.get(root.val,0)+1
            inorder(root.right,d)
            
        inorder(root,d)
        l=[]
        m=max(d.values())
        for key,val in d.items():
            if val==m:
                l.append(key)
        return l
