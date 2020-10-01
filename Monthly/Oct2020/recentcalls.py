from collections import deque

class RecentCounter:
    '''
    LeetCode Monthly Challenge for October 1st, 2020.
    '''
    def __init__(self):
        self.pings = deque()
        
    def ping(self, t: int) -> int:
        '''
        Returns the number of pings within the last 3 seconds
        (3000 milliseconds).
        
        Params:
            t - Time since the initial ping.
            
        Examples:
            rc = RecentCounter()
            rc.ping(1)      ->   1
            rc.ping(100)    ->   2
            rc.ping(3001)   ->   3
            rc.ping(3002)   ->   3
        '''
        self.pings.append(t)
        while t - self.pings[0] > 3000:
            self.pings.popleft()
            
        return len(self.pings)
