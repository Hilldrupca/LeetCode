from typing import List

class Solution:
    def fizzbuzz(self, n: int) -> List[str]:
        '''
        Convert numbers 1 to n into strings with a few exceptions. Multiples
        of 3 will output 'Fizz', multiples of 5 will output 'Buzz', and
        multiples of both will output 'FizzBuzz'.
        
        Params:
            n - End range of numbers to be converted.
            
        Returns:
            list - A list of strings for each conversion.
            
        Example:
            fizzbuzz(15)   ->   ['1','2','Fizz','4','Buzz','Fizz',
                                 '7','8','Fizz','Buzz','11','Fizz',
                                 '13','14','FizzBuzz']
        '''
        res = []
        
        for x in range(1, n+1):
            if x%3 == 0 and x%5 == 0:
                res.append('FizzBuzz')
            elif x%3 == 0:
                res.append('Fizz')
            elif x%5 == 0:
                res.append('Buzz')
            else:
                res.append(f'{x}')
            
        return res
