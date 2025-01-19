import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()        
        result = func(*args, **kwargs)
        end_time = time.time()        
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

sh = my_decorator(lambda x : print(f"Value: {x}"))
sh(123)