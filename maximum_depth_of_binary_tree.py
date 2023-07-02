class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # recursively go down the tree and keep track of the depth
        def node_depth(node, cur_depth):
            if node : 
                return max(node_depth(node.left, cur_depth+1), node_depth(node.right, cur_depth+1))
            else:
                return cur_depth

        return node_depth(root, 0)      