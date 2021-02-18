 
class Solution:
    '''
    LeetCode Monthly Challenge problem for September 10th, 2002.
    '''
    def getHint(self, secret: str, guess: str) -> str:
        '''
        Compares if digits in guess are correctly matched with digits in
        secret, and if not matched by index then shared between them. If
        A digit is at the same index in both guess and secret, it is counted
        as a bull. If a digit from guess is in secret, but has a different
        index then it is treated as a cow. Provides not hints if a digit in
        guess is not in secret.
        
        Params:
            secret - The number trying to be guessed.
            
            guess - The guessed number.
            
        Returns:
            str - The returned string will be formatted as 'xAyB'. Where 'x' is
                  the number of bull digits, and 'y' is the number of cow
                  digits.
                  
        Examples:
            getHint(secret='1807', guess='7810')   ->   '1A3B'
            getHint(secret='1123', guess='0111')   ->   '1A1B'
            getHint(secret='1122', guess='2211')   ->   '0A4B'
        '''
        cows = sum([min(guess.count(x), secret.count(x)) for x in set(guess)])
        
        bulls = 0
        for x in range(min(len(secret), len(guess))):
            if secret[x] == guess[x]:
                bulls += 1
                cows -= 1
                
        return f'{bulls}A{cows}B'
