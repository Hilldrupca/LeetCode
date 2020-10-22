import unittest, sys
sys.path.append('..')
from asteroidcollision import Solution

class TestAsteroidCollision(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_asteroid_collision(self):
        case_one = [5,10,-5]
        self.assertEqual(self.s.asteroidCollision(case_one), [5,10])
        
        
        case_two = [8,-8]
        self.assertEqual(self.s.asteroidCollision(case_two), [])
        
        
        case_three = [10,2,-5]
        self.assertEqual(self.s.asteroidCollision(case_three), [10])
        
        
        # No collisions
        case_four = [-2,-1,1,2]
        self.assertEqual(self.s.asteroidCollision(case_four), [-2,-1,1,2])
        
if __name__ == '__main__':
    unittest.main()
