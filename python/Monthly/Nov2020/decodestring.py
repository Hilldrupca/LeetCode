
class Solution:
    '''
    LeetCode Monthly Challenge problem for November 19th, 2020.
    '''
    def decodeString(self, s: str) -> str:
        '''
        Given an encoded string, returns the decoded string. The encoding rule
        is k[string]. Where is the number of times string is repeated.
        Encodings can be nested.
        
        Params:
            s - The encoded string.
            
        Returns:
            str - Decoded string.
            
        Examples:
            decodeString('3[a]2[bc]')                     ->   'aaabcbc'
            decodeString('3[a2[c]]')                      ->   'accaccacc'
            decodeString('2[abc]3[cd]ef')                 ->   'abcabccdcdcdef'
            decodeString('abc3[cd]xyz')                   ->   'abccdcdcdxyz'
            decodeString('3[z]2[2[y]pq4[2[jk]e1[f]]]ef')  ->   
                'zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef'
        '''
        repeats = []
        substrings = []
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                substrings.append(c)
            elif c == '[':
                repeats.append([num, len(substrings)])
                num = 0
            elif c == ']':
                multi, idx = repeats.pop()
                substrings += substrings[idx:] * (multi-1)
                
        return ''.join(substrings)
