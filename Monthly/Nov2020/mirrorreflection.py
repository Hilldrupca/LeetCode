from math import gcd

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 17th, 2020.
    '''
    def mirrorReflection(self, p: int, q: int) -> int:
        '''
        There is a special square room with mirrors on each of the four walls.
        Except for the southwest corner, there are receptors on each of the
        remaining corners, numbered 0, 1, and 2.
        
                   2 _____ 1
                    |     |
                    |     |
                    |_____|
                start      0
                
        The square room has walls of length p, and a laser ray from the
        southwest corner first meets the east wall at a distance q from the 0th
        receptor.

        Return the number of the receptor that the ray meets first.  (It is
        guaranteed that the ray will meet a receptor eventually.)
        
        ### Initial solution at bottom
        
        Params:
            p - Integer square wall length.
            
            q - First right wall intercept (integer).
            
        Returns:
            int - The receptor the ray meets first.
            
        Examples:
            mirrorReflection(2,1)   ->   2
            mirrorReflection(3,2)   ->   0
            mirrorReflection(4,3)   ->   2
            mirrorReflection(4,2)   ->   2
            mirrorReflection(2,2)   ->   1
        '''
        #while not (p%2 or q%2):
        #    p //= 2
        #    q //= 2
        
        g = gcd(p, q)
        p //= g
        q //= g
        
        if p%2 and not q%2:
            return 0
        elif p%2 and q%2:
            return 1
        elif not p%2 and q%2:
            return 2
        
        
        
        
        '''
        # Simulates each wall hit
        
        corners = {(p,0): 0,
                   (p,p): 1,
                   (0,p): 2}
        
        rise, run, pos = q, p, (p,q)
        while pos not in corners:
            run *= -1
            x = pos[0] + run
            y = pos[1] + rise
            
            # Recalculate y if ray intercects top wall
            if y > p:
                rise *= -1
                y = 2*p - y
                
            # Recalculate y if ray intercects bottom wall
            elif y < 0:
                y *= -1
                rise *= -1

            pos = x,y
            
        return corners[pos]
        '''
