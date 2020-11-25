
class Solution:
    '''
    LeetCode Monthly Challenge problem for November 24th, 2020.
    '''
    def calculate(self, s: str) -> int:
        '''
        Implement a basic calculator to evaluate a simple expression string.
        The expression string contains only non-negative integers, empty
        spaces, and the +, -, *, and / operators. Integer division truncates
        toward zero.
        
        Assumed that given expression is always valid.
        
        Params:
            s - Expression to evaluate.
            
        Returns:
            int - Result after evaluating expression string.
            
        Examples:
            calculate('3+2*2')       ->   7
            calculate(' 3/2 ')       ->   1
            calculate(' 3+5 / 2 ')   ->   5
        '''
        if not s:
            return 0
        
        s += '+'
        expr, num, op = [], 0, '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ':
                continue
            else:
                if op == '+':
                    expr.append(num)
                elif op == '-':
                    expr.append(-num)
                elif op == '*':
                    expr[-1] *= num
                elif op == '/':
                    expr[-1] = int(expr[-1] / num)
                op, num = c, 0
            
        return sum(expr)
