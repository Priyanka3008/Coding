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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer>result=new ArrayList<>();
        Queue<TreeNode>q= new LinkedList<>();
        q.offer(root);
        if(root==null){
            return result;
        } 
        while(!q.isEmpty()){
            TreeNode right = null;
            int size=q.size();
            for(int i=0;i<size;i++){
                TreeNode r=q.poll();
                if(r!=null){
                    right=r;
                    q.add(r.left);
                    q.add(r.right);
                }
            }
            if(right!=null){
                result.add(right.val);
            }
        }
        return result;
    }
}
