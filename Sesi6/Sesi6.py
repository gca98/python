# def my_generator():
#   print("Inside my generator")
#   yield 'a'
#   yield 'b'
#   yield 'c'

# my_generator()

# for char in my_generator():
#   print(char)

# def counter_generator(low, high):
#     while low <= high:
#        yield low
#        low += 1

# for i in counter_generator(5,10):
#   print(i, end=' ')

# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
# print()

# def square(nums):
#     result = []
 
#     for num in nums:
#         result.append(num * num)
 
#     return result
 
 
# nums = [1,2,3,4,5]
# print( square(nums) )

# def square(nums):
#     for num in nums:
#         yield (num * num)
 
 
# nums = [1,2,3,4,5]
# print( square(nums) )
 
# print( square(nums).__next__() )
# print( square(nums).__next__() )
# print( square(nums).__next__() )
# print( square(nums).__next__() )
# print( square(nums).__next__() )

# nums = [1,2,3,4,5].__iter__()
 
# print( square(nums).__next__() )
# print(next(square(nums)))
# print(next(square(nums)))
 
# squared_generator = square(nums)
# for num in squared_generator:
#     print(num)

# squared_nums = [y * y for y in [1,2,3,4,5] ]    # [1, 4, 9, 16, 25]
#               # 1 * 1 = 1
#               # 2 * 2 = 4
#               # 3 * 3 = 9
#               # 4 * 4 = 16
#               # 5 * 5 = 25
# print(squared_nums)
 
# squared_nums = [y + y for y in [1,2,3,4,5] ]
# squared_nums = [y * 4 for y in [1,2,3,4,5] ]
# squared_nums = [y + 4 for y in range(7) ]
# print(squared_nums)


# store_generator = my_generator()
# print(next(store_generator))
# print(next(store_generator))
# print(next(store_generator))


# def say_hello(name):
#     return f"Hello {name}"

# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"

# def greet_bob(greeter_func):
#     return greeter_func("Bob")

# print(greet_bob(say_hello))



# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()

# parent()

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)
# say_whee()

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

# say_whee()



# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator

# @decorator
# def say_whee():
#     print("Whee!")

# say_whee()

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1)
waste_some_time(999)
