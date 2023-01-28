/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>>result=new ArrayList<>();
        Queue<TreeNode>q=new LinkedList<>();
        if (root==null){
            return result;
        }
        q.add(root);
        while(!q.isEmpty()){
             List<Integer>r=new LinkedList<>();
             int size = q.size();
            for(int i=0;i<size;i++){
               
                TreeNode c=q.poll();
                r.add(c.val);
                if(c.left!=null){
                    q.add(c.left);
                }
                if(c.right!=null){
                    q.add(c.right);
                }
                
            }
            result.add(r);
        
        }
        return result;
        


        
    }
}
