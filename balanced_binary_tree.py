class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def tree_height(node):
            if not node : return 0
            left_height = tree_height(node.left)
            right_height = tree_height(node.right)
            if left_height < 0 or right_height < 0 or abs(left_height-right_height) > 1: return -1
            return max(left_height, right_height) + 1
        return tree_height(root) >= 0 