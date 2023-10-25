
"""
- functools.total_ordering decorator automatically provides (generate) the missing comparison 
methods (__lt__, __le__, __gt__, and __ge__) based on the provided __eq__ method 
and one other comparison method (__lt__ in this case)
 
- functools.total_orderin decorator can be used with any class that defines __eq__
and one of the comparison methods (__lt__, __le__, __gt__, or __ge__)


    """
    
    
import functools

@functools.total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __str__(self) -> str:
        return f"{self.name} has {self.age} years old"
    

if __name__ == '__main__':

    p1 = Person("Ali", 25)
    p2 = Person("Boby", 10)
    p3 = Person("Abc", 25)
    
    print("p1 < p2: ", p1 < p2)  
    print("p1 <= p3: ", p1 <= p3)  
    print("p2 > p3: ", p2 > p3)  
    print("p2 > p1: ", p2 >= p1)
    print("p1 == p3: ", p1 == p3)  
    print("p1 != p2: ", p1 != p2)  


