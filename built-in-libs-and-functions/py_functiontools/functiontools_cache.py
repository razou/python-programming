"""_summary_
- Used to memoize a function: Stores the results of a function 
call so that the function does not have to be called again if the same arguments are passed to it.
"""

import functools
import time

def factorial(n: int) -> int:
  """Calculates the factorial of n using recurrence"""
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

@functools.lru_cache(maxsize=100)
def factorial_cached(n: int) -> int:
  """Calculates the factorial of a n using memoization."""
  return factorial(n)


def fibonacci(n: int) -> int:
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

@functools.lru_cache(maxsize=100)
def fibonacci_cached(n: int) -> int:
  return fibonacci(n)


def custom_function(x):
  time.sleep(1)
  return x * x

@functools.lru_cache(maxsize=100)
def expensive_function_cached(x):
  return custom_function(x)





if __name__ == "__main__":
    
    print("************ Example with Factorial **************")
    print(factorial_cached(5))
    print(factorial_cached(5)) # use the cahsed results
    
    print("************ Example with Fibonacci **************")
    print(fibonacci_cached(10))
    print(fibonacci_cached(10)) # use cached results
    
    print("************ Example 3 **************")
    print(expensive_function_cached(5)) # => print 25, after a 1-second delay
    print(expensive_function_cached(5)) # => print 25, without a delay: using cached result
   
