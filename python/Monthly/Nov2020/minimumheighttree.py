from typing import List
from collections import defaultdict

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 4th, 2020.
    '''
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Given a tree of n nodes labelled from 0 to n-1, and a list of edges,
        returns the nodes with minimum height trees.
        
        Params:
            n - The number of nodes in the tree. Nodes will be labelled from
                0 to n-1.
                
            edges - A list of edges between nodes. Given the list
                    e = [[0,1],[1,3]], e[0] is an undirected edge between node
                    0 and node 1.
                    
        Returns:
            List[int] - Nodes with minimum height trees.
            
        Examples:
            Given the follow tree,
                    
                    3
                    |
                    1
                   / \
                  0   2
                  
            findMinHeightTrees(4, [[1,0],[1,2],[1,3]])   ->   [1]
            
            
            Given the following tree,
            
                  0
                  |
               1--3--4--5
                  |
                  2
                  
            findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])   ->   [3,4]
        '''
        if not n:
            return []
        
        if not edges:
            return [0]
        
        tree = defaultdict(set)
        for n1, n2 in edges:
            err = 'Node value {} in edge {} exceeds cap of {} - 1'
            if n1 >= n:
                raise ValueError(err.format(n1, [n1,n2], n))
            if n2 >= n:
                raise ValueError(err.format(n2, [n1,n2], n))
            
            tree[n1].add(n2)
            tree[n2].add(n1)
        
        leaf_nodes = []
        for x in tree:
            
            if len(tree[x]) == 1:
                leaf_nodes.append(x)
        
        while len(tree) > 2:
            
            next_leaves = []
            
            for node in leaf_nodes:
                
                next_node = tree.pop(node).pop()
                tree[next_node].remove(node)
                
                if len(tree[next_node]) == 1:
                    next_leaves.append(next_node)
                    
            leaf_nodes = next_leaves
            
        return list(tree.keys())
