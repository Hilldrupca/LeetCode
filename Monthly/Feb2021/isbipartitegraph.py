from collections import deque
from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for February 14th, 2021.
    '''
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        Given an undirected graph, returns if it is bipartite. Each index in
        graph is a node, and each list are the neighbors for that node.
        
        Constraints:
            len(graph) == n
            1 <= n <= 100
            0 <= len(graph[u]) < n
            0 <= graph[u][i] <= n - 1
            graph[u] does not contain u
            All values of graph[u] are unique
            If graph[u] contains v, then graph[v] contains u
            
        Params:
            graph - A list of integer lists. Indices of outer list are nodes,
                    and inner lists are neighbors of those nodes.
                    
        Returns:
            bool - If the graph is bipartite.
            
        Example:
            isBipartite([[1,3],
                         [0,2],
                         [1,3],
                         [0,2]])   ->   True
                         
            isBipartite([[1,2,3],
                         [0,2],
                         [0,1,3],
                         [0,2]])   ->   False
        '''
        colors = {}
        
        for i in range(len(graph)):
            if i not in colors and graph[i]:
                bfs = deque([i])
                colors[i] = 0
                
                while bfs:
                    node = bfs.popleft()

                    for n in graph[node]:
                        if n not in colors:
                            bfs.append(n)
                            colors[n] = colors[node] ^ 1
                        elif colors[n] == colors[node]:
                            return False

        return True
