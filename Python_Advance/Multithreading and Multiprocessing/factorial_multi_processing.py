'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorials of a given number 

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[1000, 2000, 3000, 4000, 5000,6000,700,8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]

    ############################ With Multiprocessing #############################################
    # start_time=time.time()

    # ##create a pool of worker processes
    # with multiprocessing.Pool() as pool:
    #     results=pool.map(computer_factorial,numbers)

    # end_time=time.time()

    # print(f"Results: {results}")
    # print(f"Time taken: {end_time - start_time} seconds")

    # Output: Time taken: 0.1662917137145996 seconds



    ############################ Without Multiprocessing #############################################
    start_time=time.time()
    for number in numbers:
        computer_factorial(number)
    end_time=time.time()
    print(f"Time taken: {end_time - start_time} seconds")

    # Output Time Taken: Time taken: 0.013054847717285156 seconds
    # Time taken: 0.014599800109863281 seconds


