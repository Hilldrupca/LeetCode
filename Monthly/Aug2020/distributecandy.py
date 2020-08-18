from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for August 17th, 2020.
    '''
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        '''
        Give 1 candy to the first person, 2 candies to the second person, and
        so on until we give n candies to the last person.

        Then, go back to the start of the row, giving n + 1 candies to
        the first person, n + 2 candies to the second person, and so on until
        we give 2 * n candies to the last person.
        '''
        
        # Addition only version of quadratic equation
        # Derived from the sum of natural numbers to n:
        # candies = n(n+1)/2
        num_cap = int(-.5 + (.5**.5 + 2*candies)**.5)
        
        # Create list of guaranteed numbers
        num_list = list(range(1,num_cap+1)) 
        num_list.append(candies-sum(num_list)) # Append remaining candies
        
        # Divide candies among the people and return list
        return [sum(num_list[x::num_people]) for x in range(num_people)]
