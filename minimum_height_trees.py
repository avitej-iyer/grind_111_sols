from collections import defaultdict
class Solution:

    # so this approach uses fact that in a minimum height tree, 
    # we can get to the root node by iteratively removing leaf nodes
    # and that leaf nodes are nodes with only one neighbour
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        total_nodes = n
        
        if total_nodes == 1:
            return [0]

        adj_matrix = defaultdict(set)

        # build adjacency matrix
        for src_node, dst_node in edges:
            adj_matrix[src_node].add(dst_node)
            adj_matrix[dst_node].add(src_node)
        
        # get all leaf nodes for first pass
        leaves = [node for node in adj_matrix if len(adj_matrix[node]) == 1]

        # remove leaf nodes until we have 2 or less nodes
        # because if we have 3, then one of them is a root node and two will be leaves
        # and if we have 2, then both are root nodes
        while total_nodes > 2:
            total_nodes -= len(leaves)
            
            next_leaves = []

            for x in leaves:
                # remove edge between leaf node and its neighbour
                neighbour = adj_matrix[x].pop()
                adj_matrix[neighbour].remove(x)

                # building our next set of leaves
                if len(adj_matrix[neighbour]) == 1:
                    next_leaves.append(neighbour)

            leaves = next_leaves

        return leaves            

            



        

