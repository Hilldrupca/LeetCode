import unittest, sys
sys.path.append('..')
from recentcalls import RecentCounter

class TestRecentCalls(unittest.TestCase):
    
    def setUp(self):
        self.rc = RecentCounter()
        
    def test_ping(self):
        self.assertEqual(self.rc.ping(1), 1)
        self.assertEqual(self.rc.ping(100), 2)
        self.assertEqual(self.rc.ping(3001), 3)
        self.assertEqual(self.rc.ping(3002), 3)
        
if __name__ == '__main__':
    unittest.main()
