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

            
..............................................................................................................

#String to integer(atoi)
class Solution:
    def myAtoi(self, s: str) -> int:  
        s=s.strip()
        if not s:
            return 0
        res=0
        sign=1
        if s[0]=="-":
            sign=-1
        elif s[0]=="+":
            sign=1
        elif not s[0].isdigit():
            return 0
        else:
            res=ord(s[0])-ord("0")
        for i in range(1,len(s)):
            if s[i].isdigit():
                res=res*10+(ord(s[i])-ord("0"))
            else:
                break
        res=res*sign
        if res<=-2**31:
            return -2**31
        elif res>=(2**31)-1:
            return (2**31)-1
        return res
