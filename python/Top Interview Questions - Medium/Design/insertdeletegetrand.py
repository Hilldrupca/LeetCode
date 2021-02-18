from random import randint

class RandomizedSet:
    '''
    Implement the following functions so they work in O(1) time on average.
    '''
    def __init__(self):
        self.nums_dict = {}
        self.nums_list = []
        

    def insert(self, val: int) -> bool:
        '''
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        '''
        if val not in self.nums_dict:
            self.nums_dict[val] = len(self.nums_list)
            self.nums_list.append(val)
            return True
        
        return False        

    def remove(self, val: int) -> bool:
        '''
        Removes a value from the set. Returns true if the set contained the
        specified element.
        '''
        if val in self.nums_dict:
            idx = self.nums_dict[val]
            self.nums_list[idx] = self.nums_list[-1]
            self.nums_dict[self.nums_list[idx]] = idx
            self.nums_dict.pop(val)
            self.nums_list.pop()
                
            return True
        
        return False        

    def getRandom(self) -> int:
        '''
        Get a random element from the set.
        '''
        return self.nums_list[randint(0,len(self.nums_list)-1)]
