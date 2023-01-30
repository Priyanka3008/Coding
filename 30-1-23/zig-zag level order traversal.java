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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
         List<List<Integer>>result=new ArrayList<>();
        if(root==null){
            return result;
        }
        Queue<TreeNode>q=new LinkedList<>();
        q.add(root);
        int level=0;
        while(!q.isEmpty()){
            List<Integer>r=new LinkedList<>();
            int size=q.size();
            for(int i=1;i<=size;i++){
                TreeNode c=q.poll();
                r.add(c.val);
                if(c.left!=null){
                    q.offer(c.left);
                }
                if(c.right!=null){
                    q.offer(c.right);
                }
            }
            if(level%2==1){
                Collections.reverse(r);
            }
            result.add(r);
            level++;

        } 
        return result;
        
    }
}
