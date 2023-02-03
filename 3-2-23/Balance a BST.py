# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        l=[]
        def inorder(root,l):
            if not root:
                return
            inorder(root.left,l)
            l.append(root.val)
            inorder(root.right,l)
        
        def HeightBalance(left,right):
            if right<left:
                return None
            mid=(left+right)//2
            node=TreeNode(l[mid])
            node.left=HeightBalance(left,mid-1)
            node.right=HeightBalance(mid+1,right)
            return node
        
        inorder(root,l)
        return HeightBalance(0,len(l)-1)
