class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while 1:
            if root.val > p.val and root.val>q.val:
                root = root.left
            elif root.val < q.val and root.val < p.val:
                root = root.right
            else:
                return root    