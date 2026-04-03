# Generator function that yields squares of numbers
def square_generator(n):
    for i in range(n):
        yield i ** 2

# Using the generator in a for loop
for square in square_generator(5):
    print(square)

