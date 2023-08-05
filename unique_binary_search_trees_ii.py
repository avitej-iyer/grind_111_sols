class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def generate(lo, hi):
            if lo > hi:
                return [None]
            return [TreeNode(root, left, right) for root in range(lo, hi+1) for left in generate(lo, root-1) for right in generate(root+1, hi)]
        
        return generate(1, n)