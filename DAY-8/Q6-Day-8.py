# Q6. Create a custom iterator class using __iter__ and __next__

#creating Iterator class
class Iterator:
    def __init__(self, start, end): #constructor
        self.current = start 
        self.end = end

    '''Iterable vs Iterator:
        - Iterable: Object that can return an iterator (list, tuple, string)
        - Iterator: Object that produces values one at a time
    '''
    def __iter__(self): #makes object a iterator
         # This object is its own iterator, so return self
        return self

    def __next__(self): #returns next value if value exists
        if self.current > self.end:
            raise StopIteration #necessary to stop iteration when value doesn't exists
        else:
            value = self.current
            self.current += 1
            return value  #return value

#creates counter object of Iterator class
counter = Iterator(1, 5)
for num in counter:
    print(num)  #printing result

# Manual iteration
counter2 = Iterator(10, 12)
print(next(counter2))
print(next(counter2))  
print(next(counter2))  