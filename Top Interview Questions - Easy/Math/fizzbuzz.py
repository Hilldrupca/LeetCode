from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        '''
        Returns a list of string representations of numbers from 1 to n.
        Multiples of 3 will ouput 'Fizz', multiples of 5 will output 'Buzz',
        and multiples of both 3 and 5 will output 'FizzBuzz'.
        
        Params:
            n - The end range of numbers to print.
            
        Returns:
            list[str] - The string representations of numbers.
            
        Examples:
            fizzBuzz(1)   ->   ['1']
            
            fizzBuzz(15)  ->   ['1',
                                '2',
                                'Fizz',
                                '4',
                                'Buzz',
                                'Fizz',
                                '7',
                                '8',
                                'Fizz',
                                'Buzz',
                                '11',
                                'Fizz',
                                '13',
                                '14',
                                'FizzBuzz']
        '''
        res = []
        
        for x in range(1, n+1):
            if x % 3 == 0 and x % 5 == 0:
                res.append('FizzBuzz')
            elif x % 3 == 0:
                res.append('Fizz')
            elif x % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(x))
                
        return res
