import unittest, sys
sys.path.append('..')
from skyline import Solution

class TestSkyline(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def test_get_skyline(self):
        case_one = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        
        exp_ans = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        
        with self.subTest(buildings=case_one):
            self.assertEqual(self.s.getSkyline(case_one), exp_ans)
        
        
        case_two = [[1,4,10],[2,3,11]]
        
        exp_ans = [[1,10],[2,11],[3,10],[4,0]]
        
        with self.subTest(buildings=case_two):
            self.assertEqual(self.s.getSkyline(case_two), exp_ans)
        
        
        case_three = [[0,2147483647,2147483647]]
        
        exp_ans = [[0,2147483647],[2147483647,0]]
        
        with self.subTest(buildings=case_three):
            self.assertEqual(self.s.getSkyline(case_three), exp_ans)
        
        
        case_four = [[1,2,3],[2,3,4]]
        
        exp_ans = [[1,3],[2,4],[3,0]]
        
        with self.subTest(buildings=case_four):
            self.assertEqual(self.s.getSkyline(case_four), exp_ans)
        
        
        case_five = [[1,2,1],[1,2,2],[1,2,3]]
        
        exp_ans = [[1,3],[2,0]]
        
        with self.subTest(buildings=case_five):
            self.assertEqual(self.s.getSkyline(case_five), exp_ans)
        
        
        case_six = [[2,4,7],[2,4,5],[2,4,6]]
        
        exp_ans = [[2,7],[4,0]]
        
        with self.subTest(buildings=case_six):
            self.assertEqual(self.s.getSkyline(case_six), exp_ans)
        
        
        case_seven = [[3,7,8],[3,8,7],[3,9,6],[3,10,5],[3,11,4],[3,12,3],
                      [3,13,2],[3,14,1]]
        
        exp_ans = [[3,8],[7,7],[8,6],[9,5],[10,4],[11,3],[12,2],[13,1],[14,0]]
        
        with self.subTest(buildings=case_seven):
            self.assertEqual(self.s.getSkyline(case_seven), exp_ans)
        
        
        case_eight = [[0,2,3],[2,5,3]]
        
        exp_ans = [[0,3],[5,0]]
        
        with self.subTest(buildings=case_eight):
            self.assertEqual(self.s.getSkyline(case_eight), exp_ans)
        
        
        case_nine = [[4,10,10],[5,10,9],[6,10,8],[7,10,7],[8,10,6],[9,10,5]]
        
        exp_ans = [[4,10],[10,0]]
        
        with self.subTest(buildings=case_nine):
            self.assertEqual(self.s.getSkyline(case_nine), exp_ans)
        
        
        case_ten = [[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],
                    [20,25,7]]
        
        exp_ans = [[0,7],[5,12],[10,7],[15,12],[20,7],[25,0]]
        
        with self.subTest(buildings=case_ten):
            self.assertEqual(self.s.getSkyline(case_ten), exp_ans)
            
if __name__ == '__main__':
    unittest.main()
