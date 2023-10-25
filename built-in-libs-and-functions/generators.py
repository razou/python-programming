# https://realpython.com/introduction-to-python-generators/
"""_summary_
- generator functions (or expressions) are a special kind of function that return a lazy iterator
- lazy iterators do not store their contents in memory
- call next() on a generator object 
"""
import cProfile
import sys


def compare_memory():
    n1 = int(1e4)
    n2 = int(1e5)
    n3 = int(1e6)

    print(f"list ({n1}): {sys.getsizeof([i ** 2 for i in range(n1)])} bytes")
    print(f"list ({n2}): {sys.getsizeof([i ** 2 for i in range(n2)])} bytes")
    print(f"list ({n3}): {sys.getsizeof([i ** 2 for i in range(n3)])} bytes")

    print(f"generator ({n1}): {sys.getsizeof((i ** 2 for i in range(n1)))} bytes")
    print(f"generator ({n1}): {sys.getsizeof((i ** 2 for i in range(n1)))} bytes")
    print(f"generator ({n1}): {sys.getsizeof((i ** 2 for i in range(n1)))} bytes")



if __name__ == '__main__':

    nums_squared_list = [num**2 for num in range(5)]
    nums_squared_generator = (num**2 for num in range(5))
    
    # memory optimization => sys.getsizeof() => in bytes
    # compare_memory()
    
    # computattion time
    # cProfile.run('sum([i * 2 for i in range(int(1e5))])') # list comprehension can be faster
    # cProfile.run('sum((i * 2 for i in range(int(1e5))))')

    file_name = "techcrunch.csv"
    lines = (line for line in open(file_name))
    # print(type(lines))
    # print(next(lines))
    
    list_line = (s.rstrip().split(",") for s in lines)
    # print(type(list_line))
    # print(next(list_line))

    cols = next(list_line)
    # print("cols: ", cols)
    
    company_dicts = (dict(zip(cols, data)) for data in list_line)
    # print(next(company_dicts))
    
    funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
    )

    total_series_a = sum(funding)
    print(f"total_series_a: ${total_series_a}")


    
