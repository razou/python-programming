# functools module


- The functools module in Python provides various functions for working with functions and callable objects. It offers convenient tools for functional programming and function manipulation. 
- Documentation
  - [https://docs.python.org/3/library/functools.html](https://docs.python.org/3/library/functools.html)


## `functools.partial`

- It allows to create a new function by fixing some arguments of an existing function. 
- It returns a new callable object with the specified arguments already set. 
- Uuseful when we want to create a specialized function with predefined arguments.

## `functools.partialmethod`
- Similar to partial, but designed to work with methods of classes. It creates a new method with some arguments pre-filled.

## `functools.reduce`

- It performs a reduction on a sequence using a binary function. 
- It applies the function cumulatively to the items of the sequence, from left to right, 
to reduce the sequence to a single value.



## `functools.wraps`

- It is used to create a new function wrapper that preserves the original function's metadata, such as its name, docstring, and signature. 
- It helps to maintain the identity and introspection capabilities of the wrapped function.

## `functools.cmp_to_key`  

- It converts a traditional comparison function into a key function suitable for sorting or other operations that require key-based comparisons. 
- This is useful when you have a custom comparison function and want to use it with functions that accept a key function.


##  `functools.cache`

- It is introduced in Python 3.9. 
- It provides a simple way to cache the result of a function call. 
- It remembers the results of previous function calls and returns the cached result when the same arguments are provided again. 
- This can be useful for optimizing functions that are computationally expensive or have repetitive calculations.


## `functools.lru_cache(maxsize=128)` 
- This decorator implements a memoization technique called "least recently used" (LRU) cache. It caches the results of a function's calls and avoids re-execution of the function with the same arguments. The maxsize parameter specifies the maximum number of function calls to cache.


## `functools.cached_property`
- A decorator that converts a method into a cached property, meaning the method is computed once and then cached as an attribute

## `functools.singledispatch`
- A decorator that allows you to define a generic function with specialized implementations for different types. - It is useful for creating polymorphic functions

## `functools.total_ordering`
- A decorator that provides a shortcut for defining rich comparison methods (__eq__, __ne__, __lt__, __gt__, etc.) based on a minimal set of methods.
