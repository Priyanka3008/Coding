# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1=[]
        def inorder(root,l):
            if not root:
                return 
            inorder(root.left,l)
            l.append(root.val)
            inorder(root.right,l)

        inorder(root1,list1)
        inorder(root2,list1)
        return sorted(list1)
