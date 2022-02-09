/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if(root == null) return root;
        
        Queue<Node> nodes = new LinkedList<>();
        nodes.add(root);
        
        while(!nodes.isEmpty()) {
            int size = nodes.size();
            while(size-- > 0) {
                Node cur = nodes.poll();
                if(size == 0) {
                    cur.next = null;
                } else {
                    cur.next = nodes.peek();
                }
                
                if(cur.left != null) nodes.add(cur.left);
                if(cur.right != null) nodes.add(cur.right);
            }
        }
        
        return root;
    }
}