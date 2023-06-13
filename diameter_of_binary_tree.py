# recursive approach - we use a global diameter object and 
# constantly check against it

class Solution:
    def __init__(self):
        self.diameter = 0
    
    def depth(self, node):
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        if left+right>self.diameter:
            self.diameter = left+right
        return 1 + (left if left > right else right)           

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.diameter