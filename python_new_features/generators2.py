# Infinite generator for Fibonacci numbers
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator in a for loop (limited to the first 10 Fibonacci numbers)
for fib_num in zip(range(10), fibonacci_generator()):
    print(fib_num[1])