
class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        Converts a roman numeral to an integer.
        
        Params:
            s - Roman numeral string.
            
        Returns:
            int - Roman numeral as an integer.
            
        Examples:
            romanToInt('III')       ->   3
            romanToInt('IV')        ->   4
            romanToInt('IX')        ->   9
            romanToInt('LVII')      ->   58
            romanToInt('MCMXCIV')   ->   1994
        '''
        symbol = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
        
        subtract = {'I': ('V','X'),
                    'X': ('L','C'),
                    'C': ('D','M')}
        
        total = prev = prev_count = 0
        for x in s:
            total += symbol[x]
            
            if prev in subtract and x in subtract[prev]:
                total -= 2 * symbol[prev] * prev_count
            elif prev != x:
                prev_count = 0
                
            prev = x
            prev_count += 1
            
        return total
                
