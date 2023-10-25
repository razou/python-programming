import functools


def multiply(x, y):
    return x * y

def power(base, exponent):
    return base ** exponent

def add(x, y, z):
    return x + y + z

def greet(greeting, name):
    return f"{greeting}, {name}!"



if __name__ == "__main__":
    
    

    myltiply_by_two =  functools.partial(multiply, 2) # the first argument is fixed to 2 (i.e., x = 2)
    print("myltiply_by_two(5): ", myltiply_by_two(5)) # sample as multiply(2, 5)
    
    square = functools.partial(power, exponent=2)
    print("square(5): ", square(5))
    
    cubic_score = functools.partial(power, exponent=3)
    print("cubic_score(5): ", cubic_score(5))
    

    ### Equivalent to partial(intermediate, 1), where intermediate = partial(partial, add)
    # curried_add(2) returns a new function that expects one more argument, which is then provided as (3)
    curried_add = functools.partial(functools.partial(functools.partial, add), 1) # first argument is fixed to 1
    print("curried_add(2)(3): ", curried_add(2)(3)) # equivalent to add(1,2,3), 
    print(functools.reduce(functools.partial(add, z=0), [1, 2, 3]))
    
    hello = functools.partial(greet, "Hello")
    print("hello(Sidi): ", hello("Sidi"))
    print("hello(Didi): ", hello("Didi"))



    