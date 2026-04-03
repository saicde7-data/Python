# Positional arguments (*args)
def sum_values(*args):
    result = 0
    for num in args:
        result += num
    return result

print(sum_values(1, 2, 3))  # Output: 6
print(sum_values(4, 5, 6, 7))  # Output: 22

# Keyword Arguments (**kwargs)

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

display_info(name='Alice', age=25, city='Wonderland')

# Combining *args and **kwargs

def example_function(arg1, *args, kwarg1='default', **kwargs):
    print(f'arg1: {arg1}')
    print(f'args: {args}')
    print(f'kwarg1: {kwarg1}')
    print(f'kwargs: {kwargs}')

example_function(1, 2, 3, kwarg1='custom', name='Alice', age=25)

# Output:::
# args: (2, 3)
# kwarg1: custom
# kwargs: {'name': 'Alice', 'age': 25}
