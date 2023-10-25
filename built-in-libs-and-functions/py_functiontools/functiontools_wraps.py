import functools
import math
import time

"""
functools.wraps:
- Used to create a wrapper function or decorator that preserves the metadata 
(such as the name, docstring, and other attributes) of the original function being wrapped.
- Helps to maintain important information about the original function
"""


def square_root(x: float) -> float:
    """Compute the square root of a given positive number

    Args:
        x (float): positive real number

    Returns:
        float: square root of x
    """
    
    return math.sqrt(x)


@functools.wraps(square_root)
def square_root_wrapper(x):
  """This is a square_root wrapper function."""
  print("I am wrapping square_root.")
  return square_root(x)


def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time} seconds.")
        return result
    return wrapper

@timer_decorator
def expensive_operation():
    """Perform an expensive operation."""
    time.sleep(2)
    print("Expensive operation completed.")



def custom_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@custom_decorator
def decorated_function(x: str):
    """This is a decorated function."""
    print("Executing the decorated function")
    return f"Hello {x.capitalize()}"




if __name__ == "__main__":
    
    
    print("****** Example 1 ******")
    print("square_root_wrapper example: ", square_root_wrapper(5))
    print("name: ", square_root_wrapper.__name__)
    print("doc: ", square_root_wrapper.__doc__)
    
    print("****** Example 2 ******")
    print("expensive_operation's call: ", expensive_operation())
    print("name: ", expensive_operation.__name__) 
    print("doc: ", expensive_operation.__doc__)  
    
    print("****** Example 3 ******")
    print("decorated_function's call: ", decorated_function("python"))
    print("name: ", decorated_function.__name__)  
    print("doc: ", decorated_function.__doc__) 
