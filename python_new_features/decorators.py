# Decorator function
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# Applying the decorator using @ syntax
@log_function_call
def add(a, b):
    return a + b

# Calling the decorated function
result = add(3, 5)