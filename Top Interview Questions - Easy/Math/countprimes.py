
class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        Returns how many prime numbers appear before n.
        '''
        if n < 3:
            return 0
        
        primes = [True, False] * (n//2)
        primes[0], primes[1] = False, True
        
        for x in range(3, int(n**.5)+1, 2):
            if primes[x-1]:
                for y in range(x*x, n, x):
                    primes[y-1] = False
                    
        return sum(primes)
