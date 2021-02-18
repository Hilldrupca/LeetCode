import unittest, sys
sys.path.append('..')
from clonegraph import Solution, Node

class TestCloneGraph(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_clone_graph(self):
        '''
        Graph:
            
            1 -- 2
            |    |
            |    |
            4 -- 3
        
        '''
        graph = {x: Node(x) for x in range(1, 5)}
        graph[1].neighbors = [graph[2],graph[4]]
        graph[2].neighbors = [graph[1],graph[3]]
        graph[3].neighbors = [graph[2],graph[4]]
        graph[4].neighbors = [graph[1],graph[3]]
        
        new_graph = self.s.cloneGraph(graph[1])
        
        # Ensure sizes are same
        self.assertEqual(len(graph), len(new_graph.graph()))
        
        # Ensure graph dictionaries aren't equal
        self.assertNotEqual(graph[1].graph(), new_graph.graph())
        
        
        
        
        # Ensure nothing is done if passed an empty graph
        graph = None
        self.assertIsNone(self.s.cloneGraph(graph))
        
if __name__ == '__main__':
    unittest.main()
