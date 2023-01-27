# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        result=[]
        def path(root):
            if root is None:
                result.append("N")
                return
            result.append(str(root.val))
            path(root.left)
            path(root.right)
        path(root)
        return ",".join(result)
        

    def deserialize(self, data):
        r=data.split(",")
        self.i=0
        def path():
            if r[self.i]=="N":
                self.i+=1
                return None
            a=int(r[self.i])
            node=TreeNode(a)
            self.i+=1
            node.left=path()
            node.right=path()
            return node
        return path()
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
