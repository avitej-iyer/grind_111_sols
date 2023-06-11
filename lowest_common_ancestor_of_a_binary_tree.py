class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # None - base case
        # p or q - if root is one of the targets, then the other target is  
        # obviously a descendant
        if root in (None, p, q):
            return root
        
        # you recursively go down the tree
        # checking for LCA - at the end of either left or right
        # it will return none, or a node
        left_recur, right_recur = self.lowestCommonAncestor(root.left,p,q), self.lowestCommonAncestor(root.right,p,q)

        # if both recursive calls return a node, 
        # then the lowest common ancestor is root itself
        if left_recur and right_recur:
            return root

        # if not, whichever of the two calls is not none
        # is the lowest common ancestor
        return left_recur if left_recur else right_recur 