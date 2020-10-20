from collections import deque

class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors
        
    def graph(self) -> dict:
        '''
        Returns all nodes in the graph as a dictionary. Used for testing.
        '''
        graph = {self.val: self}
        bfs = deque([self])
        while bfs:
            node = bfs.popleft()
            for n in node.neighbors:
                if n.val not in graph:
                    graph[n.val] = n
                    bfs.append(n)
                    
        return graph
    
class Solution:
    '''
    LeetCode Monthly Challenge for October 20th, 2020.
    '''
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        Performs a deep copy of a graph, and returns the new copy of the old
        reference node.
        
        # The given node will always be the first node with val = 1
        # All node values are unique
        
        Params:
            node - The 'first' node of a graph.
            
        Returns:
            'Node' - A deep copy of the reference node.
        '''
        if not node:
            return None
        
        graph = {1: Node(node.val)}
        bfs = deque([node])
        while bfs:
            old_node = bfs.popleft()
                
            for n in old_node.neighbors:
                if n.val not in graph:
                    graph[n.val] = Node(n.val)
                    bfs.append(n)
                    
                graph[old_node.val].neighbors.append(graph[n.val])
                
        return graph[1]
